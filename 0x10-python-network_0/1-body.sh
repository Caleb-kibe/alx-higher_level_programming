#!/bin/bash
# This script takes in the URL, sends a GET request to the URL
# and displays the body of the response
# Only displays the body of a 200 status code response

if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then curl -sL "$1"; fi
