#!/bin/bash

# Get the list of child directories
directories=$(find . -maxdepth 1 -type d)

# Iterate over each child directory
for directory in $directories; do
    # Skip the current directory and parent directory
    if [[ $directory != "." && $directory != ".." ]]; then
        # Remove the starting './' from the directory name
        directory=$(basename "$directory")
        # Check if pyproject.toml exists
        if [ -f "$directory/pyproject.toml" ]; then

            # Extract the version from pyproject.toml
            version=$(awk -F'"' '/^version = / {print $2}' "$directory/pyproject.toml")

            done_branch="done/$directory$version"

            # Check if the git branch exists
            if git show-ref --quiet "refs/heads/$done_branch"; then
                echo "Git branch $done_branch exists."
            else
                echo "Git branch $done_branch does not exist."
            fi
        fi
    fi
done
