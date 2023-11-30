#!/usr/bin/python3
"""Get value of `X-Request-Id` header from requested URL"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        r = get(argv[1])
        print(r.headers.get('X-Request-Id'))
    except Exception as e:
        print(e)
