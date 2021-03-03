#!/usr/bin/env python

import bitly_api
import sys

#API Authentication

API_USER = "Free: o_1982pk909d"
API_KEY =  "efe4e9161a73d48abae8e972947d374c542764fe"

bit = bitlyapi.BitLy(API_USER, API_KEY)

#lOGIC

usage = """Usage: python shortener.py [url]
e.g python shortener.py http://www.google.com"""

if len(sys.argv) != 2:
    print(usage)
    sys.exit(0)

longurl = sys.argv[1]

response = bit.shorten(longurl = longurl)

print(response['url'])






