#!/usr/bin/python3
"""Fetch URL using requests package"""

if __name__ == "__main__":
    from requests import get

    try:
        r = get('https://intranet.hbtn.io/status')
        print('Body response:')
        print('\t- type: {}'.format(type(r.text)))
        print('\t- content: {}'.format(r.text))
    except Exception as e:
        print(e)
