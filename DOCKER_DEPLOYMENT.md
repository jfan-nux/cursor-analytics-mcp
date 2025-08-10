# 🐳 Docker Deployment Guide for Cursor Analytics MCP

This guide explains how to deploy the Cursor Analytics MCP on company Docker infrastructure while allowing users to provide their own Google credentials.

## 🔧 Google Credentials Configuration Options

When hosting on Docker, users have multiple ways to provide their Google Service Account credentials:

### **Option 1: Environment Variables (Recommended)**

#### **Method A: JSON String Environment Variable**
```bash
# Set the entire JSON credentials as an environment variable
export GOOGLE_CREDENTIALS_JSON='{"type":"service_account","project_id":"your-project",...}'

# Or in Docker:
docker run -e GOOGLE_CREDENTIALS_JSON='{"type":"service_account",...}' your-mcp-image
```

#### **Method B: File Path Environment Variable**
```bash
# Mount credentials file and set path
export GOOGLE_SHEET_CREDENTIALS_FILE="/path/to/credentials.json"

# Or in Docker:
docker run -v /host/path/to/creds.json:/app/creds.json \
           -e GOOGLE_SHEET_CREDENTIALS_FILE="/app/creds.json" \
           your-mcp-image
```

#### **Method C: Default Email Override**
```bash
# Override the default sharing email
export GOOGLE_SHEETS_DEFAULT_EMAIL="user@company.com"
```

### **Option 2: Docker Volume Mount**
```bash
# Mount credentials directory
docker run -v /host/credentials:/app/credentials your-mcp-image
```

### **Option 3: Kubernetes Secrets**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: google-credentials
type: Opaque
data:
  credentials.json: <base64-encoded-service-account-json>
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cursor-analytics-mcp
spec:
  template:
    spec:
      containers:
      - name: mcp
        image: your-registry/cursor-analytics-mcp
        env:
        - name: GOOGLE_SHEET_CREDENTIALS_FILE
          value: "/etc/google-credentials/credentials.json"
        volumeMounts:
        - name: google-credentials
          mountPath: "/etc/google-credentials"
          readOnly: true
      volumes:
      - name: google-credentials
        secret:
          secretName: google-credentials
```

## 📋 User Setup Instructions

### **Step 1: Create Google Service Account**

Users need to create their own Google Service Account:

1. **Go to Google Cloud Console**: https://console.cloud.google.com/
2. **Create/Select Project**: Create a new project or select existing
3. **Enable APIs**:
   - Google Sheets API
   - Google Drive API
4. **Create Service Account**:
   - Go to "IAM & Admin" → "Service Accounts"
   - Click "Create Service Account"
   - Name: `company-mcp-sheets-service`
   - Description: `Service account for Company MCP Google Sheets`
5. **Generate Key**:
   - Click on the service account
   - Go to "Keys" tab
   - Click "Add Key" → "Create new key"
   - Choose "JSON" format
   - Download the JSON file

### **Step 2: Configure Permissions**

The service account email needs to be granted access to Google Sheets:

```
Example service account email: company-mcp-sheets@project-id.iam.gserviceaccount.com
```

**For new spreadsheets**: The MCP will automatically share with the user's email
**For existing spreadsheets**: User must manually share with the service account email

### **Step 3: Deploy with Credentials**

#### **Option A: Environment Variable (Most Secure)**
```bash
# Copy the entire JSON content and set as environment variable
export GOOGLE_CREDENTIALS_JSON='{"type":"service_account","project_id":"your-project-id",...}'
export GOOGLE_SHEETS_DEFAULT_EMAIL="your-email@company.com"

# Run the Docker container
docker run -e GOOGLE_CREDENTIALS_JSON="$GOOGLE_CREDENTIALS_JSON" \
           -e GOOGLE_SHEETS_DEFAULT_EMAIL="$GOOGLE_SHEETS_DEFAULT_EMAIL" \
           your-company/cursor-analytics-mcp:latest
```

#### **Option B: File Mount**
```bash
# Save credentials to a file
echo '{"type":"service_account",...}' > /secure/path/google-credentials.json

# Run with volume mount
docker run -v /secure/path/google-credentials.json:/app/credentials/google_sheets_credentials.json \
           -e GOOGLE_SHEETS_DEFAULT_EMAIL="your-email@company.com" \
           your-company/cursor-analytics-mcp:latest
```

## 🚀 Docker Build & Deploy

### **Dockerfile Example**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Create credentials directory
RUN mkdir -p /app/credentials

# Expose MCP port
EXPOSE 3000

# Set environment variables for better error messages
ENV PYTHONPATH=/app
ENV GOOGLE_CREDENTIALS_MISSING_OK=true

# Run the MCP server
CMD ["python", "run_server.py"]
```

### **docker-compose.yml Example**
```yaml
version: '3.8'
services:
  cursor-analytics-mcp:
    build: .
    ports:
      - "3000:3000"
    environment:
      - GOOGLE_CREDENTIALS_JSON=${GOOGLE_CREDENTIALS_JSON}
      - GOOGLE_SHEETS_DEFAULT_EMAIL=${GOOGLE_SHEETS_DEFAULT_EMAIL}
      - SNOWFLAKE_USER=${SNOWFLAKE_USER}
      - SNOWFLAKE_PASSWORD=${SNOWFLAKE_PASSWORD}
      - SNOWFLAKE_ACCOUNT=${SNOWFLAKE_ACCOUNT}
    volumes:
      - ./outputs:/app/outputs
      - ./user-analysis:/app/user-analysis
```

## 🔒 Security Best Practices

### **For Users:**
1. **Never commit credentials** to version control
2. **Use environment variables** instead of files when possible
3. **Rotate service account keys** regularly
4. **Limit service account permissions** to minimum required
5. **Use separate service accounts** for different environments

### **For Infrastructure:**
1. **Use secrets management** (Kubernetes secrets, HashiCorp Vault, etc.)
2. **Enable audit logging** for credential access
3. **Implement RBAC** for container access
4. **Scan images** for vulnerabilities
5. **Use non-root containers** when possible

## 🛠️ Troubleshooting

### **Common Issues:**

#### **"Google credentials not found"**
```bash
# Check environment variables
echo $GOOGLE_CREDENTIALS_JSON
echo $GOOGLE_SHEET_CREDENTIALS_FILE

# Verify file permissions
ls -la /path/to/credentials.json

# Test JSON validity
echo $GOOGLE_CREDENTIALS_JSON | python -m json.tool
```

#### **"Service account has no access"**
- Verify service account email is shared on the target spreadsheet
- Check that Google Sheets API and Drive API are enabled
- Ensure service account has correct IAM roles

#### **"Spreadsheet creation failed"**
- Verify Drive API is enabled
- Check service account has drive.file scope
- Ensure sufficient quota for API calls

### **Debug Mode:**
```bash
# Enable verbose logging
export MCP_DEBUG=true
export GOOGLE_API_DEBUG=true

# Run with debug output
docker run -e MCP_DEBUG=true -e GOOGLE_API_DEBUG=true your-mcp-image
```

## 📞 Support

For additional support:
1. Check the MCP logs for specific error messages
2. Verify Google Cloud Console API quotas and limits
3. Test credentials with a simple Google Sheets API call
4. Contact your infrastructure team for Docker/Kubernetes issues

## 🔄 Migration from Local Development

If moving from local development to Docker:

1. **Export current credentials**:
   ```bash
   cat cursor-analytics-mcp/keys/google_service_account_key.json
   ```

2. **Set as environment variable**:
   ```bash
   export GOOGLE_CREDENTIALS_JSON="$(cat /path/to/credentials.json)"
   ```

3. **Test locally first**:
   ```bash
   # Test with environment variable
   python run_server.py
   ```

4. **Deploy to Docker**:
   ```bash
   docker build -t cursor-analytics-mcp .
   docker run -e GOOGLE_CREDENTIALS_JSON="$GOOGLE_CREDENTIALS_JSON" cursor-analytics-mcp
   ```
