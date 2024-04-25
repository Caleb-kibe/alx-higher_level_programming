#!/bin/bash
# Checks if the URL name is provided
if [ $# -ne 1 ]; then
	exit 1
fi

# Store the URL provided as an argument
URL=$1

# Send a request to the URL using curl and store the response body in a variable
response=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Display the size of the response body in bytes
echo "$response"
