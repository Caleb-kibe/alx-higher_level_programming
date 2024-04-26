#!/bin/bash
# This script takes in a URL and displays all
# HTTP methods the server will accept
methods=$(curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-)
echo "$methods"

