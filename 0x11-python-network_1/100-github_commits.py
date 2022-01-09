#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository rails'
by the user 'rails'"""
import requests
from sys import argv


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)

    r = requests.get(url)
    try:
        r = r.json()
        for i in range(10):
            sha = r[i].get('sha')
            author = r[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author))
    except ValueError:
        print('Not a valid JSON')
