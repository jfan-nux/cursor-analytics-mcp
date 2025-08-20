# Curie Export Project - Installation and Usage Guide

This guide helps you setup the curie export tool -  export DoorDash experiment results to Google Sheets using Cursor AI. You will just need to install a few additional required packages and setup google api credentials in the correct location in the repo. All steps are performed within Cursor - no external tools needed!

## 💡 Pro Tip: Let Cursor AI Help You!

**You can use Cursor AI to help with most of these installation steps!**

**The Easiest Way:** Attach this file to the Cursor chat box and simply ask Cursor AI to follow this guide for you:
- "Can you follow the INSTALLATION_AND_USAGE.md file and help me set up the Curie export tool?"
- "Please read docs/README-curie-export.md and walk me through the setup"

**⚠️ Important:** This approach works best if you already have the latest version of the repository. If you're not sure, first ask Cursor AI: "Please help me pull the latest changes from origin main", then ask it to follow this guide from Step 2 onwards by attaching this file to the cursor chat.

**Or Ask for Specific Help:** Copy any command or step from this guide and ask Cursor AI to help you execute it:
- "Help me update my repository to get the latest code"
- "Can you help me install the additional dependencies for the curie export tool?"
- "I downloaded my Google credentials file, can you help me move it to the right place?"
- "Can you verify my installation is working?"

Cursor AI can guide you through the commands, explain what they do, and help troubleshoot any issues. You can either follow this guide manually or ask Cursor AI to walk you through each step!

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [For Existing cursor-analytics Users](#-for-existing-cursor-analytics-users)
3. [For New cursor-analytics Users](#-for-new-cursor-analytics-users)
4. [Project Structure](#project-structure)

## Prerequisites

Before starting, ensure you have:
- **Python 3.8 or newer** installed in your virtual environment
- **A Google Account** (any Gmail account works)
- **Access to DoorDash's Snowflake** data warehouse
- **Cursor IDE** installed and open with the cursor-analytics project

## 🚀 Important: Use Cursor's Terminal

**All terminal commands in this guide should be run within Cursor's integrated terminal:**

1. **Open Cursor's Terminal**:
   - Press `Ctrl+`` ` (Windows/Linux) or `Cmd+`` ` (Mac)
   - Or go to View → Terminal in Cursor's menu
   - Or click the Terminal icon in Cursor's bottom panel

2. **You'll see a terminal window** at the bottom of Cursor where you can type commands

3. **Cursor automatically starts** in your project folder, so you don't need to navigate elsewhere

---

## 🔄 For Existing cursor-analytics Users

If you already have the cursor-analytics repository in Cursor, follow these steps:

### 1. Update Your Repository

First, we need to get the latest code that includes the Curie export features.

**Option A: Ask Cursor AI** (Easiest!)
Simply tell Cursor AI: "Help me update my repository by pulling the latest changes from origin main"

**Option B: Run Commands Manually**
In Cursor's terminal (press `Ctrl+`` ` or `Cmd+`` `), run these commands:

```bash
# Get the latest updates from GitHub
# 'git fetch' checks for new changes
git fetch origin main

# Apply the updates to your local copy
# 'git pull' downloads and applies the changes
git pull origin main
```

**What these commands do:**
- `git fetch` - Checks what's new on GitHub
- `git pull` - Updates your files with the new features

### 2. Install New Dependencies

The Curie export feature needs some additional Python packages.

**Option A: Ask Cursor AI** (Easiest!)
Simply tell Cursor AI: "Help me install the additional dependencies for the curie export tool"

**Option B: Run Commands Manually**
In Cursor's terminal, run:

```bash
# Activate your Python environment
# This ensures packages install in the right place
source venv/bin/activate  # On Mac/Linux
# OR
venv\Scripts\activate     # On Windows

# Install the required Google Sheets packages
pip install gspread>=5.7.0 oauth2client>=4.1.3 gspread-formatting>=1.1.0 \
           google-auth>=2.0.0 google-api-python-client>=2.0.0

# Alternative: Update everything at once
pip install -r requirements.txt --upgrade
```

**What these do:**
- `source venv/bin/activate` - Activates your project's Python environment
- `pip install` - Installs the tools needed to create Google Sheets

### 3. Set Up Google OAuth Authentication (One-Time Setup)

This allows you to create Google Sheets under your own Google account. The tool will use OAuth to authenticate with your Google account.

#### Step 1: Create OAuth Credentials in Google Cloud Console

**💡 Cursor AI Can Help!** If you get stuck at any step, ask Cursor AI:
- "I'm at the Google Cloud Console, what should I click next?"
- "I can't find the OAuth consent screen option"
- "I downloaded the JSON file, can you move it to the correct location?"

##### 1.1 Access Google Cloud Console

1. **Open your web browser** and go to: https://console.cloud.google.com/
2. **Sign in** with your Google account
3. **Accept terms** if this is your first time

##### 1.2 Create a New Project

1. **Click the project dropdown** at the top (next to "Google Cloud")
2. **Click "NEW PROJECT"**
3. **Fill in**:
   - Project name: `curie-oauth-sheets`
   - Leave other fields as default
4. **Click "CREATE"** and wait 10-15 seconds
5. **Select your new project** from the dropdown at the top

##### 1.3 Enable Required APIs

1. **Click the menu** (☰) → **"APIs & Services"** → **"Library"**

2. **Enable Google Sheets API**:
   - Search for **"Google Sheets API"**
   - Click on it → Click **"ENABLE"**
   - Wait for it to enable

3. **Enable Google Drive API**:
   - Click **"← Library"** to go back
   - Search for **"Google Drive API"**
   - Click on it → Click **"ENABLE"**

##### 1.4 Configure OAuth Consent Screen

1. **Go to** "APIs & Services" → **"OAuth consent screen"**
2. **Select User Type**: Choose **"Internal"** → Click **"CREATE"**
3. **Fill in App Information**:
   - App name: `Curie Export Tool`
   - User support email: Select your email
   - Developer contact: Your email
   - Leave other fields empty
4. **Click "SAVE AND CONTINUE"**
5. **Scopes**: Click **"SAVE AND CONTINUE"** (no changes needed)
6. **Test users**: Click **"SAVE AND CONTINUE"** (no changes needed)
7. **Summary**: Click **"BACK TO DASHBOARD"**

##### 1.5 Create OAuth Client ID

1. **Go to** "APIs & Services" → **"Credentials"**
2. **Click "+ CREATE CREDENTIALS"** → **"OAuth client ID"**
3. **Configure**:
   - Application type: **Desktop app**
   - Name: `Curie Export Client`
4. **Click "CREATE"**
5. **Download credentials**:
   - Click **"DOWNLOAD JSON"** in the popup
   - Save the file to your Downloads folder

##### 1.6 Move Credentials to Cursor Project

**In Cursor's terminal**:

```bash
# Create credentials folder if it doesn't exist
mkdir -p credentials

# Move and rename the downloaded file
# On Mac/Linux:
mv ~/Downloads/client_secret_*.json credentials/google_oauth_credentials.json

# On Windows:
move %USERPROFILE%\Downloads\client_secret_*.json credentials\google_oauth_credentials.json

# Verify it's there
ls credentials/
```

#### Step 2: Test OAuth Authentication

Now test the authentication with a simple export:

```bash
# Navigate to project root
cd /path/to/cursorproj

# Run a test export with one metric (from project root)
python -c "
from utils.curie_export.export_helper import export_curie_with_explicit_params

# Test with a simple export
url, success, _ = export_curie_with_explicit_params(
    experiment_name='tm_negative_DxAB_canary',
    primary_metrics=['assignment_accept_rate'],
    dimension_names=['overall'],
    control_variant='15 percent',  # Specify which variant is control
    use_oauth=True
)

if success:
    print(f'✅ OAuth authentication successful!')
    print(f'📊 Test sheet created: {url}')
else:
    print('❌ Authentication failed')
"
```

**What happens during authentication:**
1. A browser window opens automatically
2. Sign in with your Google account
3. Grant permissions to the Curie Export Tool
4. Copy the authorization code shown
5. Paste it back in Cursor's terminal

**💡 Cursor AI will help!** Once credentials are set up, Cursor AI can guide you through the authentication process and help with any issues.

#### Token Storage and Management

- **Tokens are saved** in `~/.config/gspread/`
- **One-time setup** - Future exports use saved tokens
- **Auto-refresh** - Tokens refresh automatically when needed

**To re-authenticate if needed:**
```bash
# Clear cached tokens
rm -rf ~/.config/gspread/

# Run the test export again
```

### 4. Configure Default Email (Optional)

**Note**: With OAuth, sheets are created in your account so email sharing is optional. This is only needed if you want to automatically share sheets with others.

**In Cursor's terminal**:

```bash
# Save your email for automatic sharing (optional with OAuth)
echo '{"email": "{your.name@doordash.com}"}' > credentials/default_share_email.json
# Replace {your.name@doordash.com} with your actual email
# Example: echo '{"email": "john.smith@doordash.com"}' > credentials/default_share_email.json
```

### 5. Verify Installation

**Option A: Ask Cursor AI**
Just say: "Can you verify my Curie export installation is working correctly?"

**Option B: Run Tests Manually**
In Cursor's terminal, run these tests:

```bash
# Test 1: Check packages
python -c "import gspread; print('✅ Google Sheets packages installed')"

# Test 2: Check export module
python -c "from utils.curie_export import curie_to_sheets; print('✅ Curie export module available')"

# Test 3: Check OAuth setup
python -c "import os; print('✅ OAuth credentials ready' if os.path.exists('credentials/google_oauth_credentials.json') else '❌ OAuth credentials missing - see Step 3')"
```

You should see three green checkmarks (✅)!

**If any test fails**, ask Cursor AI for help: "Test 3 shows OAuth credentials missing, can you help me set it up?"

**Note**: Full authentication test happens when you run your first export (Step 3.2).

### 6. Using Cursor AI to Export (Recommended)

Now for the easy part - just talk to Cursor AI!

#### Important: Attach the Curie Export Rules

**⚠️ CRITICAL STEP**: Before asking Cursor AI to export, you must attach the rules file to help Cursor understand the proper export workflow.

1. **In Cursor's chat panel**, click the **"+" or paperclip icon** to attach a file
2. **Navigate to** `.cursor/rules/curie_export_rules.mdc`
3. **Select and attach** this file to your chat
4. **This file contains**:
   - The complete export workflow and best practices
   - How Cursor should interpret your requests
   - Validation requirements and formatting standards
   - Common pitfalls to avoid

**Why this is important**: The rules file ensures Cursor AI follows the proper workflow, asks for all necessary information, and validates the export correctly. Without it, Cursor might skip important steps or create improper exports.

#### Getting Your Analysis Name from Curie UI

**⚠️ IMPORTANT**: You must provide the exact analysis name from the Curie UI. This is the experiment name shown in the Curie platform.

**Example from Curie UI:**
In the Curie UI, the analysis name appears at the top of the experiment results page. For example:
- Analysis name: `consumer_ox_dish_exp_pizza_ui__Android_run3` (as shown in the screenshot)
- This is different from the DV config name or description

![Curie Analysis Name Example](images/curie_analysis_name_example.png)
*The analysis name "consumer_ox_dish_exp_pizza_ui__Android_run3" is highlighted at the top of the Curie experiment results page*

#### Finding Your Analysis Name in Curie

1. **Navigate to your experiment** in the Curie UI
2. **Look at the page header** - the analysis name is displayed prominently
3. **Copy the exact name** - it's typically right below the DV config name

#### Metadata Display (NEW!)

**Every export now starts with a comprehensive metadata display**. Cursor will automatically show you:

```
📊 EXPERIMENT METADATA: {experiment_name}
============================================================
Total rows: 706
Unique metrics: 61
Unique dimensions: 4

🔀 MULTI-TREATMENT EXPERIMENT (if applicable)
Variants (7): control, treatment, treatment1, treatment2, treatment3, treatment4, treatment5
Control: control
Treatments (6): treatment, treatment1, treatment2, treatment3, treatment4, treatment5

📋 Available metrics and dimensions will be displayed
📋 You'll see the planned export configuration
✅ Cursor will ask for confirmation before proceeding
```

#### Talking to Cursor AI

**In Cursor's chat** (not the terminal), simply type:

```
Export my experiment results for analysis consumer_ox_dish_exp_pizza_ui__Android_run3
```

**OAuth Note**: Cursor uses OAuth authentication. On your first export, you'll authenticate through your browser (see [Step 3](#3-set-up-google-oauth-authentication-one-time-setup) for setup).

Cursor AI will then ask you for details:

```
Cursor AI: "To export your Curie experiment results, I need the following information:

1. **Metrics** - Which metrics to include? (specific names or patterns like "all cx metrics")
2. **Metric Categorization**:
   - Primary metrics (main success metrics)
   - Secondary metrics (supporting metrics)
   - Guardrail metrics (ensure no negative impact)
3. **Dimensions** - Which dimensions for each metric? (or "overall only" for no dimensions)
4. **Cross-Dimension Filtering** (NEW!) - Want specific cuts across all metrics?
5. **Treatment Variants** (NEW!) - For multi-treatment experiments, which variants to include?
6. **Columns** - Any columns beyond the 7 defaults? (e.g., "add confidence intervals")
```

**Note about Authentication**:
- Cursor uses OAuth authentication exclusively
- Sheets are created in your Google Drive account
- No email needed unless you want to share the sheet with others

#### NEW: Cross-Dimension Filtering

You can now filter to specific dimension cuts across all metrics:

**Example: Pizza Business Analysis**
```
You: "Export experiment EHP_learning_xp_launch but only show results for pizza businesses"

Cursor: [Shows metadata including available dimension cuts]
You: "Yes, filter to ent_pizza_biz_1 (pizza businesses)"
Cursor: [Exports only pizza business results across all metrics]
```

**Example: Multiple Dimension Cuts**
```
You: "Export consumer_ox_dish_exp with results for:
- Pizza businesses (ent_pizza_biz_1)
- Weekend only (is_weekend_1)
- California markets (market_CA_1)"

Cursor: [Shows configuration with cross-dimension filtering]
```

#### NEW: Multiple Treatment Variant Support

For experiments with multiple treatments, you can select specific variants:

**Example: Multi-Treatment Export**
```
You: "Export EHP_learning_xp_launch - I want to see results for treatment1 and treatment3 only"

Cursor: [Shows all 6 available treatments]
You: "Correct, just treatment1 and treatment3 vs control"
Cursor: [Exports with selected treatments only]
```

**Example: Custom Variant Names**
```
You: "Export tm_negative_DxAB_canary experiment"

Cursor: "I see this experiment has custom variant names: '0 percent' and '15 percent'.
         Which one is the control?"
You: "15 percent is control"
Cursor: [Exports with proper control identification]
```

#### Intelligent Metric Matching

Cursor AI intelligently interprets your metric requests by:
- Searching the experiment's available metrics
- Finding semantic matches when exact names don't exist
- Suggesting the closest available metrics

**Example Interpretations**:
- "avg_item_price" → "sub_avg_item_price" (subtotal version)
- "conversion rate" → "store_level_page_conversion" (for store context)
- "revenue" → "variable_profit" or "contribution_profit" (based on description)

#### Confirmation Process

Before executing any export, Cursor will show you the complete configuration:

```
📊 Export Configuration for: consumer_ox_dish_exp_pizza_ui__Android_run3

**Metrics to Export:**
• Primary: store_level_page_conversion, dsmp_order_rate_7d
• Secondary: sub_avg_item_price, variable_profit_per_order
• Guardrail: cx_app_quality_hitch_android, core_quality_cancellation

**Dimensions:**
• Primary metrics: ent_pizza_biz
• Secondary metrics: ent_pizza_biz, overall
• Guardrail metrics: overall only

**Cross-Dimension Filters:** (if applicable)
• Only showing: ent_pizza_biz_1, is_weekend_1

**Treatment Variants:** (for multi-treatment experiments)
• Including: control, treatment1, treatment3

**Columns:**
metric_name, dimension_cut_name, control_value, treatment_value,
rel_treatment_effect, p_value, stat_sig

**Email:** analyst@doordash.com

Proceed? (y/n)
```

#### Example Conversations

**Simple Export:**
```
You: "Export consumer_ox_dish_exp_pizza_ui__Android_run3 with all metrics"
Cursor: [Shows metadata and configuration, asks for confirmation]
You: "Yes"
Cursor: [Exports and provides Google Sheets link]
```

**Cross-Dimension Export:**
```
You: "Export experiment abc_test_v2 but only for:
- New users (user_segment_new)
- Mobile orders (platform_mobile)
- Include all metrics"

Cursor: [Shows available dimension cuts and confirms selection]
You: "Perfect, proceed"
Cursor: [Exports filtered results]
```

**Multi-Treatment Export:**
```
You: "Export EHP_learning_xp_launch with:
- Primary: dasher pay metrics
- Only show treatment2 and treatment4 results
- Break down by crash dimension"

Cursor: [Shows 6 available treatments, confirms selection]
You: "Yes, that's right"
Cursor: [Exports with selected treatments only]
```

**Advanced Combined Example:**
```
You: "Export analysis multi_variant_pricing_test with:
- Primary: conversion and revenue metrics
- Secondary: average basket metrics
- Show only results for pizza restaurants in California
- Include treatments: low_price and medium_price variants only
- Add confidence intervals"

Cursor: [Shows detailed configuration with all filters]
You: "Looks good, proceed"
Cursor: [Exports with all specifications]
```

#### Export Formats

**Single Treatment Experiments** (backward compatible):
- Pivoted format: control_value | treatment_value | rel_treatment_effect
- Standard column names maintained

**Multi-Treatment Experiments** (NEW!):
- Unpivoted format: variant_name | variant_value | rel_effect
- Each treatment appears as a separate row
- Dimension cuts are visually merged in Google Sheets

#### Common Commands

```
# Basic export with analysis name from Curie UI
"Export experiment results for analysis consumer_ox_dish_exp_pizza_ui__Android_run3"

# With cross-dimension filtering
"Export analysis abc_test only for pizza businesses and weekend orders"

# With specific treatment variants
"Export multi_treatment_exp showing only treatment1 and treatment3"

# Combined advanced request
"Export pricing_test_v3 with:
- Conversion metrics only
- Pizza businesses in CA markets
- Show treatment_low and treatment_high variants
- Include confidence intervals"
```

### 7. Alternative: Terminal Commands

If you prefer typing commands, you can use Cursor's terminal with Python one-liners:

```bash
# Basic OAuth export (from project root)
python -c "from utils.curie_export.export_helper import export_curie_with_explicit_params; url, success, _ = export_curie_with_explicit_params(experiment_name='your_experiment_name', primary_metrics=['metric1', 'metric2'], use_oauth=True); print(f'Sheet URL: {url}' if success else 'Export failed')"

# Example with real experiment:
python -c "from utils.curie_export.export_helper import export_curie_with_explicit_params; url, success, _ = export_curie_with_explicit_params(experiment_name='consumer_ox_dish_exp_pizza_ui__Android_run3', primary_metrics=['store_level_page_conversion'], use_oauth=True); print(f'Sheet URL: {url}' if success else 'Export failed')"

# With multiple options:
python -c "
from utils.curie_export.export_helper import export_curie_with_explicit_params
url, success, _ = export_curie_with_explicit_params(
    experiment_name='your_experiment_name',
    primary_metrics=['metric1', 'metric2'],
    secondary_metrics=['metric3'],
    dimension_names=['overall'],
    use_oauth=True
)
print(f'Sheet URL: {url}' if success else 'Export failed')
"
```

**Note**: These are complex one-liners. The AI method through Cursor's chat is much easier!

### 8. Your Exported Sheet

After export, you'll get:
- **A Google Sheets link** - Click to view
- **Multiple tabs**: All Metrics, Primary, Secondary, Guardrail
- **Professional formatting** with color-coded significance

### 9. If Something Goes Wrong

**Easiest Solution: Ask Cursor AI!**
Just describe your problem to Cursor AI:
- "I'm getting an authentication error when trying to export"
- "The export says it can't find my credentials file"
- "My export failed with an error about missing packages"

Cursor AI can help diagnose and fix most issues!

**Manual Troubleshooting:**
In Cursor's terminal, you can check:

```bash
# See your current location
pwd

# Check credentials exist
ls credentials/

# View recent errors
tail -20 logs/curie_export.log
```

**Common fixes:**
- Make sure you're in the cursor-analytics folder
- Verify credentials file exists
- Check you copied the exact analysis name from Curie
- Try again after some time - The source tables can take upto 4 hours to update after you rerun the analysis on the Curie UI

### 10. Advanced Usage (For Experienced Users)

#### Using OAuth in Commands

OAuth is now the default authentication method. When using Python to export:

```python
# In a Python script or interactive session
from utils.curie_export.export_helper import export_curie_with_explicit_params

export_curie_with_explicit_params(
    experiment_name='my_experiment',
    primary_metrics=['metric1'],
    use_oauth=True  # Always use OAuth
)

# Or as a one-liner in terminal
python -c "from utils.curie_export.export_helper import export_curie_with_explicit_params; export_curie_with_explicit_params(experiment_name='my_experiment', primary_metrics=['metric1'], use_oauth=True)"
```

#### Command Line Options

**Column Selection (from project root):**
```python
# Default columns (7 essential)
from utils.curie_export.export_helper import export_curie_with_explicit_params

export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["metric1"],
    selected_columns=None,  # Uses default 7 columns
    use_oauth=True
)

# Custom column selection
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["metric1"],
    selected_columns=["metric_name", "dimension_cut_name", "control_value",
                      "treatment_value", "rel_treatment_effect", "p_value", "stat_sig"],
    use_oauth=True
)

# All available columns
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["metric1"],
    selected_columns=["metric_name", "dimension_cut_name", "dimension_name",
                      "control_value", "treatment_value", "rel_treatment_effect",
                      "p_value", "stat_sig", "control_unit_count", "treatment_unit_count",
                      "abs_treatment_effect", "abs_treatment_effect_ci_lower",
                      "abs_treatment_effect_ci_upper", "rel_treatment_effect_ci_lower",
                      "rel_treatment_effect_ci_upper", "analyzed_at"],
    use_oauth=True
)
```

**Metric and Dimension Filtering:**
```python
# Filter specific metrics by category
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["store_conversion_rate", "order_rate_7d"],
    secondary_metrics=["avg_item_price"],
    guardrail_metrics=["cancellation_rate"],
    use_oauth=True
)

# Overall results only (no dimension cuts)
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate"],
    dimension_names=["overall"],
    use_oauth=True
)

# Specific dimensions for all metrics
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate"],
    dimension_names=["city", "user_segment", "ent_pizza_biz"],
    use_oauth=True
)

# Specific dimension cuts (exact cuts)
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate"],
    dimension_cuts=["city_SF", "ent_pizza_biz_1", "is_weekend_1"],
    use_oauth=True
)
```

**Advanced: Per-Metric Dimension Mapping:**
```python
# Different dimensions for different metrics
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate", "order_value"],
    secondary_metrics=["customer_satisfaction"],
    metric_dimension_map={
        "conversion_rate": {
            "names": ["city", "user_segment"],  # Get all cuts for these dimensions
            "cuts": []  # No specific cuts
        },
        "order_value": {
            "names": [],  # No dimension names
            "cuts": ["ent_pizza_biz_1", "is_weekend_1"]  # Only these specific cuts
        },
        "customer_satisfaction": {
            "names": ["overall"],  # Overall only
            "cuts": []
        }
    },
    use_oauth=True
)
```

**Multi-Treatment Experiments:**
```python
# Select specific treatment variants
export_curie_with_explicit_params(
    experiment_name="multi_treatment_exp",
    primary_metrics=["conversion_rate"],
    treatment_variants=["treatment_1", "treatment_3"],  # Only these treatments vs control
    use_oauth=True
)

# Custom control variant name
export_curie_with_explicit_params(
    experiment_name="custom_variant_exp",
    primary_metrics=["conversion_rate"],
    control_variant="15 percent",  # Specify which variant is control
    use_oauth=True
)
```

**Additional Options:**
```python
# Specify Google Drive folder for organization
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate"],
    folder_id="your_google_drive_folder_id",  # Organize sheets in specific folder
    use_oauth=True
)

# Export to CSV only (no Google Sheets)
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate"],
    export_to_sheets=False,  # Will save as CSV instead
    use_oauth=True
)

# Share with specific email
export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate"],
    share_email="colleague@doordash.com",  # Share with specific person
    use_oauth=True
)
```

**Python API Usage (from project root):**
```python
# Always import from root directory
from utils.curie_export.export_helper import export_curie_with_explicit_params

# Advanced export with OAuth
url, success, detected_control = export_curie_with_explicit_params(
    experiment_name="my_experiment",
    primary_metrics=["conversion_rate", "order_value"],
    secondary_metrics=["customer_satisfaction"],
    dimension_names=["city", "user_segment"],
    selected_columns=None,  # Use default columns
    use_oauth=True
)

if success:
    print(f"Export completed!")
    print(f"Sheet URL: {url}")
    print(f"Detected control variant: {detected_control}")
```

**Export to CSV Only (No Google Sheets):**
```python
# Import from root directory
from utils.curie_export.curie_to_sheets import load_curie_results, export_to_csv

# Load data without creating Google Sheet
df = load_curie_results("my_experiment")
csv_path = export_to_csv(df, "my_experiment")
print(f"CSV saved to: {csv_path}")

# Load with filtering
df = load_curie_results(
    analysis_name="my_experiment",
    metrics=["conversion_rate", "order_rate"],
    dimensions=["overall", "city"]
)
```

**Available Columns:**
- **Default (7)**: metric_name, dimension_cut_name, control_value, treatment_value, rel_treatment_effect, p_value, stat_sig
- **Additional**: metric_definition, metric_category, metric_subcategory, metric_importance, metric_desired_direction, control_unit_count, treatment_unit_count, control_stddev, treatment_stddev, abs_treatment_effect, abs_treatment_effect_ci_lower, abs_treatment_effect_ci_upper, rel_treatment_effect_ci_lower, rel_treatment_effect_ci_upper, analyzed_at

**Performance Tips:**
- Use `selected_columns=None` for default columns to reduce data transfer
- Filter metrics/dimensions to only what you need
- Default queries are already optimized

---

## 🆕 For New cursor-analytics Users

### Already Completed

If you followed the README to set up cursor-analytics in Cursor:
- ✅ Code is downloaded
- ✅ Python packages installed

### Continue Setup

Now do these steps from above:
1. **[Step 3: OAuth Setup](#3-set-up-google-oauth-authentication-one-time-setup)** - Simple browser authentication
2. **[Step 4: Configure Email](#4-configure-default-email-optional)** - Optional for OAuth users
3. **[Step 5: Verify](#5-verify-installation)** - Check it works
4. **[Step 6: Export with AI](#6-using-cursor-ai-to-export-recommended)** - Start exporting!

### Your First Export

Once setup is done, just ask Cursor:

```
"Export my experiment {your_experiment_name} with all metrics"
```

That's it! Cursor AI handles everything else.

## Remember

- **Cursor AI is your assistant** - Ask for help with ANY step in this guide!
- **All terminal commands** run in Cursor's integrated terminal (`Ctrl+`` ` or `Cmd+`` `)
- **Talk to Cursor AI** in the chat panel for the easiest experience
- **Keep Cursor open** throughout the entire process
- **The feature is designed for Cursor** - it won't work well in external terminals

## Quick Start with Cursor AI

Instead of reading this entire guide, you can simply:

1. **First, ensure you have the latest code**: Ask Cursor AI: "Please help me pull the latest changes from origin main"
2. **Then ask Cursor AI to follow this guide**: "Please follow the docs/INSTALLATION_AND_USAGE.md file and help me set up Curie export"
   - Or simply: "Help me set up the Curie export tool following the installation guide"
3. **OAuth is automatic**: When you run your first export, Cursor will guide you through OAuth authentication
4. **Ask questions** whenever you're unsure
5. **Get help** with any errors or issues

The AI-assisted approach is often faster and easier than following the manual steps!

**Quick OAuth Export Example**:
```
You: "Export experiment my_experiment_name with OAuth"
Cursor: [Opens browser for authentication on first use, then exports your data]
```



The Curie Export Project automates the process of:
1. **Extracting** experiment results from DoorDash's Curie experimentation platform
2. **Processing** the data with statistical analysis and formatting
3. **Exporting** to Google Sheets with professional formatting and validation

## Architecture Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Snowflake     │────▶│  Python Export   │────▶│  Google Sheets  │
│ (Curie Tables)  │     │     Pipeline     │     │   (Formatted)   │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                               │
                               ▼
                        ┌──────────────┐
                        │ Configuration │
                        │ & Validation  │
                        └──────────────┘
```

## Project Structure

```
cursorproj/
├── docs/                                 # Documentation
│   ├── CODEBASE_OVERVIEW.md             # This file
│   └── INSTALLATION_AND_USAGE.md        # Setup and usage guide
├── local_tools/curie_export/             # Main export module
│   ├── config.py                        # Configuration constants
│   ├── curie_to_sheets.py              # Main export orchestrator
│   ├── google_sheets_formatter.py       # Google Sheets API & formatting
│   ├── test_formatting.py              # Formatting validation
│   ├── export_helper.py                # Helper utilities
│   ├── export_curie_experiment.py      # CLI script
│   ├── export_curie.sh                 # Shell wrapper
│   └── sql/                            # SQL query templates
│       └── combined_curie_results_v2.sql
├── credentials/                         # API credentials (gitignored)
│   └── google_sheets_credentials.json
└── requirements.txt                     # Python dependencies
```

## Core Components

### 1. **Export Orchestration (`export_helper.py`)**
High-level orchestration layer that manages the entire export workflow:
- **User-facing API**: `export_curie_with_explicit_params()` function
- **Metadata Display**: Shows comprehensive experiment information before export
- **Parameter Validation**: Ensures all inputs are valid before processing
- **Control Detection**: Intelligently identifies control variants
- **Error Resolution**: Guides users through any configuration issues

### 2. **Data Pipeline (`curie_to_sheets.py`)**
Main data operations layer that handles experiment data:
- **SQL Execution**: Runs queries against Snowflake using `combined_curie_results_unified.sql`
- **Format Detection**: Identifies single vs multi-treatment experiments
- **Data Transformation**: Pivots single treatments, renames multi-treatment columns
- **Data Filtering**: Applies metric, dimension, and variant filters
- **OAuth Management**: Handles Google OAuth authentication

### 3. **Google Sheets Integration (`google_sheets_formatter.py`)**
Handles all Google Sheets operations with enterprise-grade reliability:
- **Authentication**: Both service account and OAuth support
- **JSON Serialization**: Comprehensive handling of NaN/inf values
- **Rate Limiting**: Adaptive rate limiting with exponential backoff
- **Formatting Pipeline**: Headers, numbers, conditional formatting, merging
- **Error Recovery**: Automatic retry with formatting state preservation

### 4. **Configuration System (`config.py`)**
- Centralizes all settings for export behavior
- Defines column selections (default, custom, all)
- Manages Google Sheets formatting specifications
- Contains database table references and statistical thresholds

### 5. **SQL Data Layer (`sql/combined_curie_results_unified.sql`)**
- Single unified query for all experiments
- Returns unpivoted data format
- Includes all treatment variants
- Supports multi-treatment analysis

### 6. **Validation System (`test_formatting.py`)**
Ensures export quality through comprehensive checks:
- **Structure Validation**: Verifies data placement and headers
- **Format Validation**: Confirms number formatting and styling
- **Visual Validation**: Checks merging, borders, and conditional formatting
- **Success Criteria**: Only reports SUCCESS when all validations pass
