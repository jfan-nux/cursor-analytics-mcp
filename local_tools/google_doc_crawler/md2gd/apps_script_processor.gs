/**
 * Google Docs Crawler - Apps Script Processor
 * 
 * This script processes Google Docs created by the crawler/sync tool.
 * It finds [img][path] markers and replaces them with actual images from Drive.
 * It finds [table]...[/table] markers and replaces them with actual tables.
 * It also applies template styles (fonts, etc.).
 * 
 * Usage:
 * 1. Deploy this as an API Executable in Apps Script
 * 2. For personal accounts: Use Script ID from Project Settings
 * 3. For Workspace accounts: Use Deployment ID (starts with AKfyc...)
 * 4. Add the ID to config.yaml as apps_script_id
 */

/**
 * Main function to process a document.
 * Finds image markers and replaces them with actual images across all tabs.
 * Finds table markers and replaces them with actual tables across all tabs.
 * Applies template styles to all content across all tabs.
 * 
 * Note: Even when tabId is provided, we process all tabs because:
 * 1. Apps Script Tab objects don't have a reliable way to get tab IDs
 * 2. Python already scopes the content update to the specific tab
 * 3. Processing all tabs ensures consistency (e.g., if images reference same file)
 * 
 * @param {string} documentId - The ID of the document to process
 * @param {string} templateDocId - The ID of the template document with styles
 * @param {string} tabId - Ignored (kept for API compatibility)
 * @return {object} Result object with success status and message
 */
function processDocument(documentId, templateDocId, tabId) {
  try {
    const doc = DocumentApp.openById(documentId);
    
    // Get all tabs in the document (handles both tabbed and non-tabbed docs)
    // We process all tabs regardless of tabId parameter because Python
    // already scoped the content update to the specific tab
    const allTabs = getAllTabs(doc);
    
    let totalImagesInserted = 0;
    let totalTablesInserted = 0;
    
    // Process each tab
    for (const tab of allTabs) {
      const documentTab = tab.asDocumentTab();
      const body = documentTab.getBody();
      
      // Check if this tab has any markers before processing
      // This prevents corrupting already-processed tabs
      const bodyText = body.getText();
      const hasImageMarkers = bodyText.includes('[img][');
      const hasTableMarkers = bodyText.includes('[table]');
      
      // Log what we found
      const tabTitle = documentTab.getTitle ? documentTab.getTitle() : 'Unknown';
      Logger.log(`Tab: ${tabTitle}, hasImageMarkers: ${hasImageMarkers}, hasTableMarkers: ${hasTableMarkers}`);
      
      if (!hasImageMarkers && !hasTableMarkers) {
        // Skip this tab - already processed or no markers
        Logger.log(`Skipping tab: ${tabTitle}`);
        continue;
      }
      
      Logger.log(`Processing tab: ${tabTitle}`);
      
      // Step 1: Replace image markers with actual images in this tab
      const imageResult = insertImagesFromMarkers(body);
      totalImagesInserted += imageResult.count;
      
      // Step 2: Replace table markers with actual tables in this tab
      const tableResult = insertTablesFromMarkers(body);
      totalTablesInserted += tableResult.count;
      
      // Step 3: Apply template styles to this tab (optional)
      // NOTE: Can destroy formatting. Use with caution.
      // if (templateDocId) {
      //   applyTemplateStylesToBody(body, templateDocId);
      // }
    }
    
    return {
      success: true,
      message: `Processed ${allTabs.length} tab(s) successfully. ${totalImagesInserted} images inserted, ${totalTablesInserted} tables inserted.`,
      imagesInserted: totalImagesInserted,
      tablesInserted: totalTablesInserted,
      tabsProcessed: allTabs.length,
      stylesApplied: false
    };
    
  } catch (error) {
    return {
      success: false,
      message: `Error processing document: ${error.toString()}`,
      error: error.toString()
    };
  }
}

/**
 * Returns a flat list of all tabs in the document, in the order
 * they would appear in the UI (i.e. top-down ordering). Includes
 * all child tabs.
 * 
 * Based on Google's official documentation:
 * https://developers.google.com/apps-script/guides/docs/tabs
 * 
 * @param {GoogleAppsScript.Document.Document} doc - The document
 * @return {Array<GoogleAppsScript.Document.Tab>} List of all tabs
 */
function getAllTabs(doc) {
  const allTabs = [];
  // Iterate over all tabs and recursively add any child tabs to
  // generate a flat list of Tabs.
  for (const tab of doc.getTabs()) {
    addCurrentAndChildTabs(tab, allTabs);
  }
  return allTabs;
}

/**
 * Adds the provided tab to the list of all tabs, and recurses
 * through and adds all child tabs.
 * 
 * @param {GoogleAppsScript.Document.Tab} tab - The tab to add
 * @param {Array<GoogleAppsScript.Document.Tab>} allTabs - The list to add to
 */
function addCurrentAndChildTabs(tab, allTabs) {
  allTabs.push(tab);
  for (const childTab of tab.getChildTabs()) {
    addCurrentAndChildTabs(childTab, allTabs);
  }
}

/**
 * Find and replace [img][path] markers with actual images from Drive.
 * 
 * @param {GoogleAppsScript.Document.Body} body - The document body
 * @return {object} Result with count of images inserted
 */
function insertImagesFromMarkers(body) {
  try {
    const pattern = '\\[img\\]\\[([^\\]]+)\\]';
    
    // Get page dimensions for image sizing
    const pageWidthPts = body.getPageWidth();
    const marginLeftPts = body.getMarginLeft();
    const marginRightPts = body.getMarginRight();
    const availableWidthPts = pageWidthPts - marginLeftPts - marginRightPts;
    
    // Convert to image units (Docs uses 96 DPI for images, 72 for points)
    const POINTS_PER_INCH = 72;
    const IMAGE_DPI = 96;
    const availableWidthPx = Math.round(availableWidthPts * IMAGE_DPI / POINTS_PER_INCH);
    
    // Collect all matches first to avoid mutation issues
    const matches = [];
    let result = body.findText(pattern);
    while (result) {
      matches.push(result);
      result = body.findText(pattern, result);
    }
    
    if (matches.length === 0) {
      return { count: 0, message: 'No image markers found' };
    }
    
    // Process from last to first so offsets remain valid
    let insertedCount = 0;
    for (let i = matches.length - 1; i >= 0; i--) {
      try {
        const rangeEl = matches[i];
        const textEl = rangeEl.getElement().asText();
        const start = rangeEl.getStartOffset();
        const endIncl = rangeEl.getEndOffsetInclusive();
        const fullText = textEl.getText();
        const matchText = fullText.substring(start, endIncl + 1);
        
        // Extract path from marker
        const pathMatch = matchText.match(/^\[img\]\[([^\]]+)\]$/i);
        if (!pathMatch) {
          continue;
        }
        const path = pathMatch[1].trim();
        if (!path) {
          continue;
        }
        
        // Find file in Drive by path
        const file = resolveDriveFileByPath(path);
        if (!file) {
          Logger.log(`Could not find file: ${path}`);
          continue;
        }
        
        const blob = file.getBlob();
        
        // Delete the marker text WITHOUT destroying formatting
        textEl.deleteText(start, endIncl);
        
        // Insert image at the position where the marker was
        const paragraph = textEl.getParent().asParagraph();
        const childIndex = paragraph.getChildIndex(textEl);
        
        // If we deleted at the start of the text element, insert before it
        // Otherwise, insert after it
        const insertPosition = (start === 0) ? childIndex : childIndex + 1;
        const inlineImage = paragraph.insertInlineImage(insertPosition, blob);
        
        // Resize image to fit available width, preserving aspect ratio
        try {
          const imgWidthUnit = inlineImage.getWidth();
          const imgHeightUnit = inlineImage.getHeight();
          
          if (imgWidthUnit > availableWidthPx) {
            const scale = availableWidthPx / imgWidthUnit;
            const targetHeightUnit = Math.round(imgHeightUnit * scale);
            
            inlineImage.setWidth(availableWidthPx);
            inlineImage.setHeight(targetHeightUnit);
          }
        } catch (resizeErr) {
          Logger.log(`Could not resize image: ${resizeErr}`);
        }
        
        insertedCount++;
        
      } catch (imgErr) {
        Logger.log(`Error processing image marker: ${imgErr}`);
      }
    }
    
    return { count: insertedCount, message: `Inserted ${insertedCount} images` };
    
  } catch (error) {
    Logger.log(`Error in insertImagesFromMarkers: ${error}`);
    return { count: 0, message: error.toString() };
  }
}

/**
 * Find and replace [table]...[/table] markers with actual tables.
 * 
 * @param {GoogleAppsScript.Document.Body} body - The document body
 * @return {object} Result with count of tables inserted
 */
function insertTablesFromMarkers(body) {
  try {
    let insertedCount = 0;
    
    // Get all text as a string to find markers
    const fullText = body.getText();
    Logger.log(`Full document text length: ${fullText.length}`);
    
    // Find table markers using regex
    const tablePattern = /\[table\]([\s\S]*?)\[\/table\]/g;
    let match;
    const tablesToInsert = [];
    
    while ((match = tablePattern.exec(fullText)) !== null) {
      const tableData = match[1].trim();
      const startPos = match.index;
      const endPos = match.index + match[0].length;
      
      Logger.log(`Found table marker at ${startPos}-${endPos}`);
      Logger.log(`Table data: ${tableData.substring(0, 100)}...`);
      
      tablesToInsert.push({
        startPos: startPos,
        endPos: endPos,
        data: tableData
      });
    }
    
    if (tablesToInsert.length === 0) {
      Logger.log('No table markers found');
      return { count: 0, message: 'No table markers found' };
    }
    
    // PASS 1: Insert all tables (in reverse order to preserve positions)
    Logger.log('PASS 1: Inserting all tables...');
    for (let i = tablesToInsert.length - 1; i >= 0; i--) {
      try {
        const tableInfo = tablesToInsert[i];
        const tableData = tableInfo.data;
        
        // Parse table data - each row starts with [row]
        const rows = tableData.split('\n').filter(row => row.trim());
        if (rows.length === 0) {
          Logger.log('No rows in table data');
          continue;
        }
        
        // Parse each row - strip [row] marker and split by |
        const parsedRows = rows.map(row => {
          const cleanRow = row.replace(/^\[row\]/, '').trim();
          return cleanRow.split('|').map(cell => cell.replace(/&#124;/g, '|').trim());
        });
        
        const numRows = parsedRows.length;
        const numCols = Math.max(...parsedRows.map(r => r.length));
        
        Logger.log(`Creating table with ${numRows} rows and ${numCols} columns`);
        
        // Find the paragraph containing the start of the marker
        let targetPara = null;
        const paragraphs = body.getParagraphs();
        let charCount = 0;
        
        for (let p = 0; p < paragraphs.length; p++) {
          const para = paragraphs[p];
          const paraText = para.getText();
          const paraStart = charCount;
          const paraEnd = charCount + paraText.length + 1; // +1 for newline
          
          if (paraStart <= tableInfo.startPos && tableInfo.startPos < paraEnd) {
            targetPara = para;
            Logger.log(`Found target paragraph at index ${p}`);
            break;
          }
          
          charCount = paraEnd;
        }
        
        if (!targetPara) {
          Logger.log('Could not find target paragraph');
          continue;
        }
        
        // Insert table before the target paragraph
        const paraIndex = body.getChildIndex(targetPara);
        const table = body.insertTable(paraIndex);
        
        // Populate table
        for (let r = 0; r < numRows; r++) {
          const row = table.appendTableRow();
          const rowData = parsedRows[r];
          
          for (let c = 0; c < numCols; c++) {
            const cellText = c < rowData.length ? rowData[c] : '';
            
            // Check for formatting markers {B}text{/B} and {I}text{/I}
            const hasBold = cellText.includes('{B}');
            const hasItalic = cellText.includes('{I}');
            
            // Strip the markers to get clean text
            let cleanText = cellText;
            cleanText = cleanText.replace(/\{B\}/g, '').replace(/\{\/B\}/g, '');
            cleanText = cleanText.replace(/\{I\}/g, '').replace(/\{\/I\}/g, '');
            
            const cell = row.appendTableCell(cleanText);
            
            // Apply formatting based on markers or header row
            if (cleanText) {
              const text = cell.editAsText();
              // Bold if: header row OR has {B} marker
              text.setBold(r === 0 || hasBold);
              // Italic if: has {I} marker
              if (hasItalic) {
                text.setItalic(true);
              }
            }
          }
        }
        
        insertedCount++;
        
      } catch (tableErr) {
        Logger.log(`Error inserting table: ${tableErr}`);
      }
    }
    
    // PASS 2: Clean up all marker paragraphs in one pass
    Logger.log('PASS 2: Removing all marker paragraphs...');
    const parasToRemove = [];
    
    for (let p = 0; p < body.getNumChildren(); p++) {
      const child = body.getChild(p);
      if (child.getType() === DocumentApp.ElementType.PARAGRAPH) {
        const text = child.asParagraph().getText();
        // Remove paragraphs containing table or row markers
        if (text.includes('[table]') || text.includes('[/table]') || text.includes('[row]')) {
          parasToRemove.push(p);
        }
      }
    }
    
    // Remove in reverse order to maintain indices
    for (let idx = parasToRemove.length - 1; idx >= 0; idx--) {
      const paraIdx = parasToRemove[idx];
      try {
        if (paraIdx < body.getNumChildren()) {
          body.removeChild(body.getChild(paraIdx));
          Logger.log(`Removed marker paragraph at index ${paraIdx}`);
        }
      } catch (err) {
        Logger.log(`Could not remove paragraph ${paraIdx}: ${err}`);
      }
    }
    
    return { count: insertedCount, message: `Inserted ${insertedCount} tables` };
    
  } catch (error) {
    Logger.log(`Error in insertTablesFromMarkers: ${error}`);
    return { count: 0, message: error.toString() };
  }
}

/**
 * Resolve a Drive file by its path.
 * Path format: "GoogleDocCrawler_Images/project/subfolder/image.png"
 * 
 * @param {string} path - The Drive path to the file
 * @return {GoogleAppsScript.Drive.File} The Drive file, or null if not found
 */
function resolveDriveFileByPath(path) {
  try {
    const parts = String(path).split('/').filter(p => p && p.trim() !== '');
    if (parts.length === 0) {
      return null;
    }
    
    const fileName = parts[parts.length - 1];
    const firstSegment = parts[0];
    
    // Find the root folder
    const candidateRoots = DriveApp.getFoldersByName(firstSegment);
    
    while (candidateRoots.hasNext()) {
      let currentFolder = candidateRoots.next();
      let validPath = true;
      
      // Walk down each folder segment
      for (let i = 1; i < parts.length - 1; i++) {
        const segment = parts[i];
        const subFolders = currentFolder.getFoldersByName(segment);
        if (!subFolders.hasNext()) {
          validPath = false;
          break;
        }
        currentFolder = subFolders.next();
      }
      
      if (!validPath) {
        continue;
      }
      
      // Find the file by name in the final folder
      const files = currentFolder.getFilesByName(fileName);
      if (files.hasNext()) {
        return files.next();
      }
    }
    
    return null;
    
  } catch (error) {
    Logger.log(`Error in resolveDriveFileByPath: ${error}`);
    return null;
  }
}

/**
 * Apply template styles to a specific body (tab).
 * NOTE: This can destroy formatting. Use with caution and extensive testing.
 * 
 * @param {GoogleAppsScript.Document.Body} body - The body to style
 * @param {string} templateDocId - The template document ID with styles
 * @return {object} Result object
 */
function applyTemplateStylesToBody(body, templateDocId) {
  try {
    if (!templateDocId) {
      return { stylesApplied: false, message: 'No template document specified' };
    }
    
    // Get template document
    const templateDoc = DocumentApp.openById(templateDocId);
    const templateBody = templateDoc.getBody();
    
    // Get template's font settings
    const templateAttrs = templateBody.getTextAttributes();
    const templateFont = templateAttrs[DocumentApp.Attribute.FONT_FAMILY];
    const templateFontSize = templateAttrs[DocumentApp.Attribute.FONT_SIZE];
    
    // Get template styles for headings
    const heading1Style = templateBody.getHeadingAttributes(DocumentApp.ParagraphHeading.HEADING1);
    const heading2Style = templateBody.getHeadingAttributes(DocumentApp.ParagraphHeading.HEADING2);
    const heading3Style = templateBody.getHeadingAttributes(DocumentApp.ParagraphHeading.HEADING3);
    
    // Apply to all paragraphs in this body
    const paragraphs = body.getParagraphs();
    for (let i = 0; i < paragraphs.length; i++) {
      const para = paragraphs[i];
      const heading = para.getHeading();
      
      try {
        // Apply paragraph-level style based on heading type
        switch (heading) {
          case DocumentApp.ParagraphHeading.HEADING1:
            para.setAttributes(heading1Style);
            break;
          case DocumentApp.ParagraphHeading.HEADING2:
            para.setAttributes(heading2Style);
            break;
          case DocumentApp.ParagraphHeading.HEADING3:
            para.setAttributes(heading3Style);
            break;
        }
        
        // Apply font to all text in this paragraph (trying to preserve bold/italic)
        const text = para.editAsText();
        const textLength = text.getText().length;
        
        if (textLength > 0 && templateFont) {
          text.setFontFamily(0, textLength - 1, templateFont);
          if (templateFontSize) {
            text.setFontSize(0, textLength - 1, templateFontSize);
          }
        }
      } catch (paraErr) {
        Logger.log(`Could not style paragraph ${i}: ${paraErr}`);
      }
    }
    
    // Apply font to all tables in this body
    const tables = body.getTables();
    for (let t = 0; t < tables.length; t++) {
      try {
        const table = tables[t];
        const numRows = table.getNumRows();
        
        for (let r = 0; r < numRows; r++) {
          const row = table.getRow(r);
          const numCells = row.getNumCells();
          
          for (let c = 0; c < numCells; c++) {
            const cell = row.getCell(c);
            const cellText = cell.editAsText();
            const cellLength = cellText.getText().length;
            
            if (cellLength > 0 && templateFont) {
              cellText.setFontFamily(0, cellLength - 1, templateFont);
              if (templateFontSize) {
                cellText.setFontSize(0, cellLength - 1, templateFontSize);
              }
            }
          }
        }
      } catch (tableErr) {
        Logger.log(`Could not style table ${t}: ${tableErr}`);
      }
    }
    
    return { stylesApplied: true, message: 'Template styles applied successfully' };
    
  } catch (error) {
    Logger.log(`Error in applyTemplateStylesToBody: ${error}`);
    return { stylesApplied: false, message: error.toString() };
  }
}

