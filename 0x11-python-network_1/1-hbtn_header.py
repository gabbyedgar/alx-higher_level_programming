#!/usr/bin/python3
"""Script to make a request to a url passed on the command line"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.getheader('X-Request-Id'))
    except (urllib.error.URLError, IndexError) as e:
        print(e)
