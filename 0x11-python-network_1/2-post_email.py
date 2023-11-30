#!/usr/bin/python3
"""Send a POST request to a url with the payload being an email address"""

import urllib.parse
import urllib.request
import urllib.error
import sys

try:
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode()
    with urllib.request.urlopen(sys.argv[1], data=data) as r:
        print(r.read().decode('utf8'))
except (urllib.error.URLError, IndexError) as e:
    print(e)
