#!/bin/bash
# Migrate global mapping to local

GLOBAL_FILE=~/.gdocs_sync_mappings.json
LOCAL_FILE=./.gdocs_sync_mappings.json

if [ -f "$GLOBAL_FILE" ] && [ ! -f "$LOCAL_FILE" ]; then
    echo "Migrating global mapping to local..."
    cp "$GLOBAL_FILE" "$LOCAL_FILE"
    echo "✅ Migrated successfully!"
    echo "Local mapping file: $LOCAL_FILE"
    echo ""
    echo "You can now delete the global file if you want:"
    echo "  rm $GLOBAL_FILE"
elif [ -f "$LOCAL_FILE" ]; then
    echo "Local mapping file already exists: $LOCAL_FILE"
else
    echo "No global mapping file found to migrate."
fi
