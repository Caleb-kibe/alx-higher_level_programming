#!/bin/bash
# This script takes in the URL, sends a GET request to the URL
# and displays the body of the response
# Only displays the body of a 200 status code response

url="$1"

response=$(curl -s "$url")

status_code=$(echo "$response" | head -n 1 | cut -d ' ' -f2)

if [[ "$status_code" -eq 200 ]]; then
	body=$(echo "$response" | sed '/^$/d')
	echo "$body"
fi
