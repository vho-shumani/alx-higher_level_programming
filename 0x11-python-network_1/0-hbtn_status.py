#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as reponse:
    body_response = reponse.read()
print("Body response:")
print(f"\t- type: {type(body_response)}")
print(f"\t- content: {body_response}")
print(f"\t- utf8 content: {body_response.decode('utf-8')}")
