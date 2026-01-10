/**
 * Markdown Google Docs Sync - Apps Script Processor
 * 
 * This script processes Google Docs created by the markdown sync tool.
 * It finds [img][path] markers and replaces them with actual images from Drive.
 * It also finds [table]...[/table] markers and creates proper tables.
 * 
 * Note: Template styling is now handled by the Python client using the
 * Google Docs API's updateNamedStyle requests, which properly preserves
 * bold/italic formatting in tables. The templateDocId parameter is kept
 * for API compatibility but is not used by this script.
 * 
 * Usage:
 * 1. Deploy this as a web app or library
 * 2. Call processDocument(documentId) after each export
 */

/**
 * Main function to process a document.
 * Finds image markers and replaces them with actual images across all tabs.
 * Finds table markers and replaces them with proper tables.
 * 
 * Note: Even when tabId is provided, we process all tabs because:
 * 1. Apps Script Tab objects don't have a reliable way to get tab IDs
 * 2. Python already scopes the content update to the specific tab
 * 3. Processing all tabs ensures consistency (e.g., if images reference same file)
 * 
 * @param {string} documentId - The ID of the document to process
 * @param {string} templateDocId - Unused (kept for API compatibility; styling now handled by Python)
 * @param {string} tabId - Unused (kept for API compatibility)
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
      const hasPersonMarkers = bodyText.includes('[person:');
      
      // Log what we found
      const tabTitle = documentTab.getTitle ? documentTab.getTitle() : 'Unknown';
      Logger.log(`Tab: ${tabTitle}, hasImageMarkers: ${hasImageMarkers}, hasTableMarkers: ${hasTableMarkers}, hasPersonMarkers: ${hasPersonMarkers}`);
      
      if (!hasImageMarkers && !hasTableMarkers && !hasPersonMarkers) {
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
      
      // Step 3: Replace person markers with person chips in this tab
      const personResult = insertPersonChipsFromMarkers(body);
      Logger.log(`Inserted ${personResult.count} person chips`);
      
      // Note: Template styling is now handled by Python using updateNamedStyle
      // which properly preserves bold/italic formatting in tables
    }
    
    return {
      success: true,
      message: `Processed ${allTabs.length} tab(s) successfully. ${totalImagesInserted} images inserted, ${totalTablesInserted} tables inserted.`,
      imagesInserted: totalImagesInserted,
      tablesInserted: totalTablesInserted,
      tabsProcessed: allTabs.length
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
        
        // Track cells to merge: [{row, col, rowSpan}]
        const mergeCells = [];
        
        // Populate table
        for (let r = 0; r < numRows; r++) {
          const row = table.appendTableRow();
          const rowData = parsedRows[r];
          
          for (let c = 0; c < numCols; c++) {
            let cellText = c < rowData.length ? rowData[c] : '';
            
            // Check for merge markers [merge:N] where N is the number of rows to span
            const mergeMatch = cellText.match(/^\[merge:(\d+)\]/);
            if (mergeMatch) {
              const rowSpan = parseInt(mergeMatch[1], 10);
              mergeCells.push({ row: r, col: c, rowSpan: rowSpan });
              cellText = cellText.replace(/^\[merge:\d+\]/, '');
              Logger.log(`Found merge marker at row ${r}, col ${c}, spanning ${rowSpan} rows`);
            }
            
            // Check for [merged] marker (cells that will be merged away)
            const isMerged = cellText === '[merged]';
            if (isMerged) {
              cellText = '';  // Clear the marker, cell will be merged
            }
            
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
        
        // Apply cell merges (must be done after table is fully populated)
        for (const merge of mergeCells) {
          try {
            const startCell = table.getRow(merge.row).getCell(merge.col);
            // Merge cells vertically
            // Note: Google Apps Script Table doesn't have a direct merge API
            // We need to use a workaround: clear the cells that should be merged
            // and set vertical alignment. True merging requires the advanced Docs API.
            // For now, we'll just leave the repeated content cleared (already done above)
            Logger.log(`Would merge cell at row ${merge.row}, col ${merge.col} spanning ${merge.rowSpan} rows`);
            // TODO: If true merging is needed, use the Advanced Docs API
          } catch (mergeErr) {
            Logger.log(`Error processing merge: ${mergeErr}`);
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
 * Path format: "MarkdownSync_Images/project/subfolder/image.png"
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
 * Web app entry point for HTTP requests.
 * Allows calling the script via URL.
 * 
 * @param {object} e - Event parameter with query parameters
 * @return {GoogleAppsScript.Content.TextOutput} JSON response
 */
function doGet(e) {
  const documentId = e.parameter.documentId;
  const templateDocId = e.parameter.templateDocId;
  
  if (!documentId) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      message: 'Missing documentId parameter'
    })).setMimeType(ContentService.MimeType.JSON);
  }
  
  const result = processDocument(documentId, templateDocId);
  
  return ContentService.createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Replaces [person:email:Name] markers with actual person chips (smart chips).
 * 
 * @param {Body} body - The document body to process
 * @return {object} Result with count of person chips inserted
 */
function insertPersonChipsFromMarkers(body) {
  try {
    let insertedCount = 0;
    
    // Pattern to find person markers: [person:email@domain.com:Display Name]
    const personPattern = /\[person:([^\]:]+):([^\]]+)\]/g;
    
    // We need to process markers one at a time because inserting a person chip
    // changes the document structure
    let processedAny = true;
    let iterations = 0;
    const maxIterations = 100; // Safety limit
    
    while (processedAny && iterations < maxIterations) {
      processedAny = false;
      iterations++;
      
      const fullText = body.getText();
      const match = personPattern.exec(fullText);
      
      if (match) {
        const email = match[1];
        const displayName = match[2];
        const markerStart = match.index;
        const markerText = match[0];
        
        Logger.log(`Found person marker: ${displayName} <${email}> at position ${markerStart}`);
        
        // Find the element containing this marker
        const searchResult = body.findText(escapeRegex(markerText));
        
        if (searchResult) {
          const element = searchResult.getElement();
          const startOffset = searchResult.getStartOffset();
          const endOffset = searchResult.getEndOffsetInclusive();
          
          // Get the parent paragraph
          let parent = element;
          while (parent && parent.getType() !== DocumentApp.ElementType.PARAGRAPH) {
            parent = parent.getParent();
          }
          
          if (parent) {
            const paragraph = parent.asParagraph();
            
            // Delete the marker text first
            if (element.getType() === DocumentApp.ElementType.TEXT) {
              const textElement = element.asText();
              textElement.deleteText(startOffset, endOffset);
            }
            
            // Insert the person chip at the position where the marker was
            // Note: insertPerson is not available on Text elements, only on certain containers
            // We'll insert the person at the cursor position in the paragraph
            try {
              // Try to use the Person chip API (available in newer Apps Script)
              const personBuilder = paragraph.insertText(startOffset, displayName);
              
              // Unfortunately, Apps Script doesn't have a direct way to insert Person chips
              // via the Document API. The best we can do is insert the email as a mailto link.
              // Person chips require the UI or the Docs API (not Apps Script).
              
              // Create a mailto link as the best fallback
              const text = paragraph.editAsText();
              const nameLength = displayName.length;
              text.setLinkUrl(startOffset, startOffset + nameLength - 1, 'mailto:' + email);
              
              insertedCount++;
              processedAny = true;
              
            } catch (chipErr) {
              Logger.log(`Could not insert person chip, using mailto link: ${chipErr}`);
              // Fallback: just insert the display name with a mailto link
              const text = paragraph.editAsText();
              text.insertText(startOffset, displayName);
              text.setLinkUrl(startOffset, startOffset + displayName.length - 1, 'mailto:' + email);
              insertedCount++;
              processedAny = true;
            }
          }
        }
        
        // Reset regex for next iteration
        personPattern.lastIndex = 0;
      }
    }
    
    Logger.log(`Inserted ${insertedCount} person chips/links`);
    return { count: insertedCount, message: `Inserted ${insertedCount} person chips` };
    
  } catch (error) {
    Logger.log(`Error in insertPersonChipsFromMarkers: ${error}`);
    return { count: 0, message: error.toString() };
  }
}

/**
 * Escapes special regex characters in a string.
 */
function escapeRegex(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/**
 * POST endpoint (same functionality as GET).
 */
function doPost(e) {
  return doGet(e);
}

