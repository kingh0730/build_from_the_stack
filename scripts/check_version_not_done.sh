#!/bin/bash

# Change to the parent directory
cd "$(dirname "$0")"

# Get the list of child directories
directories=$(find . -maxdepth 1 -type d)

# Iterate over each child directory
for directory in $directories; do
    # Skip the current directory and parent directory
    if [[ $directory != "." && $directory != ".." ]]; then
        # Check if pyproject.toml exists
        if [ -f "$directory/pyproject.toml" ]; then
            # Extract the version from pyproject.toml
            version=$(awk -F= '/^version/ { gsub(/[[:blank:]]/, "", $2); print $2 }' "$directory/pyproject.toml")

            # Check if the git branch exists
            if git show-ref --quiet "refs/heads/$directory$version"; then
                echo "Git branch $directory$version exists."
            else
                echo "Git branch $directory$version does not exist."
            fi
        fi
    fi
done
