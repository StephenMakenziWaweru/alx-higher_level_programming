#!/usr/bin/python3
"""takes url & email, sends a POST request and displays the response"""
from urllib.request import Request, urlopen
from urllib.error import URLError
from sys import argv


req = Request(argv[1])
try:
    with urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))
except URLError as e:
    if hasattr(e, 'code'):
        print('Error code:', e.code)
