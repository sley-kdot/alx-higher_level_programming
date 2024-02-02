#!/usr/bin/python3
"""
module contains a script that takes in a URL, sends a request to the URL
and displays the value
"""
import urllib.request
import sys

if __name__ == "__main__":
    user_agent = {'user-Agent': user}
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.header)