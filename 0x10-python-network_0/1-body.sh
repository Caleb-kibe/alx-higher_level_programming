#!/bin/bash
# This script takes in the URL, sends a GET request to the URL
# and displays the body of the response
# Only displays the body of a 200 status code response

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Define the URL from the argument
url="$1"

# Use curl to get the response with silent mode (-s)
response=$(curl -s "$url")

# Extract the status code using cut
status_code=$(echo "$response" | head -n 1 | cut -d ' ' -f2)

# Check if status code is 200
if [ "$status_code" -eq 200 ]; then
  # Remove headers using sed (delete everything before the first empty line)
  body=$(echo "$response" | sed '/^$/d')
  echo "$body"
else
  echo "Error: Status code is not 200 (Found: $status_code)"
fi
