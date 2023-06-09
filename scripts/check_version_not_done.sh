#!/bin/bash

# Get the current directory
current_dir=$(pwd)

# Loop through each child directory
for dir in "$current_dir"/*/; do
    # Check if the child directory has a pyproject.toml file
    if [ -f "$dir/pyproject.toml" ]; then
        # Change into the child directory
        cd "$dir"

        # Extract the version from pyproject.toml
        version=$(awk -F= '/^version/ { gsub(/[[:blank:]]/, "", $2); print $2 }' "$directory/pyproject.toml")

        # Check if the git branch exists
        if git show-ref --quiet "refs/heads/$directory$version"; then
            echo "Git branch $directory$version exists."
        else
            echo "Git branch $directory$version does not exist."
        fi

        # Change back to the original directory
        cd "$current_dir"
    fi
done
