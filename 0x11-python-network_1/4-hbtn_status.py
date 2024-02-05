#!/usr/bin/python3
"""
module includes a script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    status = response.text
    print("Body response:")
    print(f"\t- type: {type(status)}")
    print(f"\t- content: {status}")
