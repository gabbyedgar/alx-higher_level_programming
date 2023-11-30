#!/usr/bin/python3
"""Script to request content from `https://intranet.hbtn.io/status`"""

import urllib.request
import urllib.error

try:
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        body = r.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf8')))
except urllib.error.URLError as e:
    print(e)
