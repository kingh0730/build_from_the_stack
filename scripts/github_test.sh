#!/bin/bash

# List of directory names
directories=("dir1" "dir2" "dir3")

# Loop through each directory
for dir in "${directories[@]}"; do
    # Change into the directory
    cd "$dir"

    # Run 'tox' command
    python -m tox -e py

    # Change back to the original directory
    cd -
done
