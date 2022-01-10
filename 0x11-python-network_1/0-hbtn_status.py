#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status with urlib"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        r = response.read()
        p = "Body response:\n\t- type: {}\n\t- content: {}"
        p += "\n\t- utf8 content: {}"
        print(p.format(type(r), r, r.decode('utf-8')))
