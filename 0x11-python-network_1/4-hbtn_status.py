#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
          type(r.text), r.text))
