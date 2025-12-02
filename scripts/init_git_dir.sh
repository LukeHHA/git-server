#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="/srv/git"

# Create the directory (and parents if needed)
sudo mkdir -p "$TARGET_DIR"

# Get current user and primary group
USER_NAME="$(id -un)"
GROUP_NAME="$(id -gn)"

# Change owner and group to the current user
sudo chown "$USER_NAME:$USER_NAME" "$TARGET_DIR"

# Optional: set permissions (read/write/execute for user only)
sudo chmod 700 "$TARGET_DIR"

echo "Initialized $TARGET_DIR owned by $USER_NAME:$USER_NAME)"