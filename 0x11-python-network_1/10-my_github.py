#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the GitHub
API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
    headers = {'Authorization': f'token {argv[2]}'}
    r = requests.get('https://api.github.com/user', headers=headers)
    r = r.json()
    print(r.get('id'))
