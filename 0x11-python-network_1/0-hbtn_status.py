#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status with urlib"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        r = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(r), r, r.decode('utf-8')))
