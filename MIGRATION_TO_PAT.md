# Migration from Username/Password to Personal Access Token (PAT)

## Summary
Successfully migrated Snowflake authentication from username/password to Personal Access Token (PAT) authentication.

## Changes Made

### 1. Core Connection Module (`utils/snowflake_connection.py`)

#### Updated `__init__` method:
- Changed parameter from `password` to `token`
- Updated environment variable from `SNOWFLAKE_PASSWORD` to `SNOWFLAKE_PAT`
- Removed password-based authentication
- Updated docstring to reflect PAT authentication
- Note: PAT authentication uses the default authenticator (no need to specify oauth)

#### Updated `params` dictionary:
```python
# Note: Snowflake PAT tokens are passed via the 'password' parameter
self.params = dict(
    user=self.user,
    password=self.token,    # PAT token passed as password (not as 'token')
    schema=self.schema,
    account=self.account,
    database=self.database,
    warehouse=self.warehouse,
    role=self.role,
    insecure_mode=insecure_mode,
)
```

**Important**: Snowflake's Python connector expects PAT tokens to be passed via the `password` field, not as a separate `token` field. This is by design in the Snowflake connector.

#### Updated `_validate_params` method:
- Changed validation from `password` to `token`

#### Updated Spark connection parameters (`sfparams`):
```python
# Note: Snowflake PAT tokens are passed via the password field
self.sfparams = dict(
    sfUrl=f"{self.account}.snowflakecomputing.com",
    sfAccount=self.account,
    sfUser=self.user,
    sfPassword=self.token,    # PAT token passed as password
    sfDatabase=self.database,
    sfSchema=self.schema,
    sfWarehouse=self.warehouse,
    sfRole=self.role
)
```

### 2. Documentation Updates

#### `USAGE_EXAMPLES.md`:
- Updated error handling section to reference `SNOWFLAKE_PAT` instead of `SNOWFLAKE_PASSWORD`

#### `install.sh`:
- Updated installation instructions to show `SNOWFLAKE_PAT` instead of `SNOWFLAKE_PASSWORD`

## Migration Guide for Users

### Important Note About Snowflake PAT Implementation

**Key Implementation Detail**: While we store the token in `SNOWFLAKE_PAT` environment variable (to distinguish it from password-based auth), the Snowflake Python connector expects PAT tokens to be passed via the `password` parameter. This is by design in the Snowflake connector - PAT tokens are treated as password equivalents for authentication purposes.

### Required Environment Variable Changes

**Old configuration:**
```bash
export SNOWFLAKE_USER='your.username'
export SNOWFLAKE_PASSWORD='your_password'
```

**New configuration:**
```bash
export SNOWFLAKE_USER='your.username'
export SNOWFLAKE_PAT='your_personal_access_token'
```

**What happens internally**: 
- We read from `SNOWFLAKE_PAT` env var
- We pass it to Snowflake connector via the `password` field
- This allows us to use PAT authentication while keeping our code semantically clear

### How to Generate a Personal Access Token

1. Log into Snowflake via the web interface
2. Navigate to your user profile
3. Go to "Personal Access Tokens" section
4. Click "Generate New Token"
5. Give it a descriptive name (e.g., "cursor-analytics-mcp")
6. Set expiration as needed
7. Copy the token and set it as `SNOWFLAKE_PAT` environment variable

### Updating Your Configuration

1. **In your shell profile** (`.zshrc`, `.bashrc`, etc.):
   ```bash
   # Remove or comment out:
   # export SNOWFLAKE_PASSWORD='your_password'
   
   # Add:
   export SNOWFLAKE_PAT='your_personal_access_token'
   ```

2. **In your `.env` file** (if using `config/.env`):
   ```bash
   # Remove:
   # SNOWFLAKE_PASSWORD=your_password
   
   # Add:
   SNOWFLAKE_PAT=your_personal_access_token
   ```

3. **Reload your shell**:
   ```bash
   source ~/.zshrc  # or source ~/.bashrc
   ```

### Benefits of PAT Authentication

1. **Enhanced Security**: PATs can be scoped with specific permissions
2. **Token Rotation**: Easy to rotate without changing your actual password
3. **Audit Trail**: Better tracking of which applications are accessing Snowflake
4. **No Password Storage**: Eliminates the need to store passwords in environment variables

## Testing the Migration

After updating your environment variables, test the connection:

```bash
source venv/bin/activate
python -c "from utils.snowflake_connection import SnowflakeHook; sf = SnowflakeHook(); sf.connect(); print('Connection successful!')"
```

## Backward Compatibility

⚠️ **Important**: This change is **NOT backward compatible**. 

- All users must update their environment variables from `SNOWFLAKE_PASSWORD` to `SNOWFLAKE_PAT`
- The code will no longer accept password-based authentication
- Existing scripts and configurations using `SNOWFLAKE_PASSWORD` will fail

## Files Modified

1. `utils/snowflake_connection.py` - Core authentication logic
2. `USAGE_EXAMPLES.md` - Documentation update
3. `install.sh` - Installation instructions update
4. `MIGRATION_TO_PAT.md` - This migration guide (NEW)

## Date of Migration

November 6, 2025

