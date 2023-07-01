#!/bin/bash

# Exist on error
set -e

# Get the current directory
current_dir=$(pwd)

# Loop through each child directory
for dir in "$current_dir"/*/; do
    # Check if the child directory has a pyproject.toml file
    if [ -f "$dir/pyproject.toml" ]; then
        # Change into the child directory
        cd "$dir"

        # Run 'install' command
        python -m pip install -e ".[dev,test]"

        # Change back to the original directory
        cd "$current_dir"
    fi
done
