#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
 the value of the X-Request-Id variable found in the header of the response
 """
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    post_data = urllib.parse.urlencode({'email': argv[2]}).encode('ascii')
    with urllib.request.urlopen(url=argv[1], data=post_data) as response:
        print(response.read().decode('UTF-8'))
