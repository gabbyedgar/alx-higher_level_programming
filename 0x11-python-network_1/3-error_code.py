#!/usr/bin/python3
"""Script that sends URL request and prints status code on error,
or the body on success."""


if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
