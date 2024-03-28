#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests
if __name__ == "__main__":
    if len(sys.argv) < 2:
        lett = ""
    else:
        lett = sys.argv[1]
    try:
        req = requests.post('http://0.0.0.0:5000/search_user', data={'q': lett})
        json_data = req.json()
        if json_data:
            print(f'[{json_data.get("id"}] {json_data.get("name")}')
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
