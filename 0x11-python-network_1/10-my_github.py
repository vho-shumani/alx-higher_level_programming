#!/usr/bin/python3
"""that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    json_data = req.json()
    user_id = json_data.get('id')
    print(user_id)
