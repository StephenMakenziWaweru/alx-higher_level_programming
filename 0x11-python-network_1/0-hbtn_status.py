#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status with urlib"""
from urllib import request


if __name__ == '__main__':
    req = request.Request("https://intranet.hbtn.io/status")
    with request.urlopen(req) as response:
        r = response.read()
        s = "Body response:\n\t- type: {}\n\t- content: {}"
        s += "\n\t- utf8 content: {}"
        print(s.format(type(r), r, r.decode('utf-8')))
