#!/bin/bash
# Catch me
curl "0.0.0.0:5000/catch_me" -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98"
