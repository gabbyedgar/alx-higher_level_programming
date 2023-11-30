#!/usr/bin/python3
"""Get GitHub id using github API along with Basic Authentication"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
        j = r.json()
        print(j.get('id'))
    except ValueError as e:
        print(e)
