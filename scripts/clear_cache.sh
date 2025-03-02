#!/bin/bash

curr_dir=$(basename "$PWD")
if [ "$curr_dir" != "tverbatch" ]; then
    echo "Error: This script can only be executed in the tverbatch directory!"
    exit 1
fi

cache_dirs=$(find "$PWD" -type d \( -name "__pycache__" -o -name ".pytest_cache" \))
if [ -z "$cache_dirs" ]; then
    echo "No __pycache__ or .pytest_cache directories found."
else
    cache_count=$(echo "$cache_dirs" | wc -l)

    echo "Deleting [$cache_count] cache directories..."
    echo "$cache_dirs" | xargs rm -rf
    echo "[$cache_count] cache directories successfully deleted."
fi
