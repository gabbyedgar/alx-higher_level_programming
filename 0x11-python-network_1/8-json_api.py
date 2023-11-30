#!/usr/bin/python3
"""Send a POST request to the specified URL in the variable 'q'"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    try:
        if len(argv) < 2:
            letter = ""
        else:
            letter = argv[1]
        r = post('http://0.0.0.0:5000/search_user', data={'q': letter})
        j = r.json()
        if not j:
            print('No result')
        else:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
    except ValueError:
        print('Not a valid JSON')
