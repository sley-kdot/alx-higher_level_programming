#!/bin/bash
# Bash script that sends a JSON POST request to a URL
curl -d "@$2" -H "Content-Type: application/json" -sX POST "$1"
