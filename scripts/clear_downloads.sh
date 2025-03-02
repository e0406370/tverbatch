#!/bin/bash

folder="downloads"

file_count=$(find "$folder" -type f | wc -l)
echo "Found [$file_count] files in [$folder]."

if [ "$file_count" -gt 0 ]; then
    for file in "$folder"/*; do
        if [ -f "$file" ]; then
            echo "Deleting $file"
            rm "$file"
        fi
    done

    echo "[$file_count] files in [$folder] successfully deleted."
else
    echo "No files to delete."
fi
