#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -o /dev/null -s -L -w "%{http_code}" "$1"
