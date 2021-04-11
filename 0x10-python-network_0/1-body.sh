#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ "$(curl -sLw "%{http_code}" "$1" -o /dev/null)" -eq "200" ]; then curl -sL "$1"; fi # curl -sIL "$1" | grep "HTTP/1.0 200 OK" > /dev/null && curl -sL "$1"
