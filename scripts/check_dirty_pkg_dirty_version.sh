#!/bin/bash

set -e

# Manually set the last clean commit hash
last_clean_commit="3c01cbd27607081b7c86104c4513cf22a47e3600"

# Get the last commit hash
last_commit=$(git rev-parse HEAD)

# Find the modified directories using git diff-tree
modified_directories=$(
    git diff-tree --no-commit-id --name-only -r \
        "$last_clean_commit" "$last_commit" |
        xargs -I {} dirname {} |
        sort -u
)

# Print the modified directories
for dir in $modified_directories; do
    echo "$dir has been modified."

    # Get the top-level directory of the dir variable
    dir=$(echo "$dir" | awk -F'/' '{print $1}')

    if [ -f "$dir/pyproject.toml" ]; then
        # Extract the version from pyproject.toml
        version=$(awk -F'"' '/^version = / {print $2}' "$dir/pyproject.toml")

        done_branch="done/$dir/$version"

        # Check if the git branch exists
        if git ls-remote --exit-code --heads origin $done_branch; then
            echo "Git branch $done_branch exists, NOT_OK!"
        else
            echo "Git branch $done_branch does not exist, OK."
        fi
    fi
done
