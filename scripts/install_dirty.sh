#!/bin/bash

set -e

# Manually set the last clean commit hash
last_clean_commit="5a4d6e09973d1ec4b7486b5e0c9fdb5b337bc02d"

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

    if [ -f "$dir/pyproject.toml" ]; then
        # Extract the version from pyproject.toml
        version=$(awk -F'"' '/^version = / {print $2}' "$dir/pyproject.toml")

        done_branch="done/$dir/$version"

        # Check if the git branch exists
        if git ls-remote --exit-code --heads origin $done_branch; then
            echo "Git branch $done_branch exists, NOT_OK!"

            # Raise an error
            exit 1

        else
            echo "Git branch $done_branch does not exist, OK."

            # Install the package
            python -m pip install -e "$dir[dev,test]"
        fi
    fi
done
