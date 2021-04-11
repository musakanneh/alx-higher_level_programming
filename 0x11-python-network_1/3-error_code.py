#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            s = response.read()
            print(s.decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
