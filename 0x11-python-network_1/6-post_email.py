#!/usr/bin/python3
"""
Python script that takes in a URL and
an email address, sends a POST request
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
