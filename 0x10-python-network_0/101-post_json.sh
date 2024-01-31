#!/bin/bash
# Bash script that sends a JSON POST request to a URL
curl -d "@$2" -sX POST "$1"
