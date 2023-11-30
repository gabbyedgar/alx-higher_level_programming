#!/usr/bin/python3
"""Script to query the Star Wars API based on command line argument"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        r = get('https://swapi.co/api/people/', params={'search': argv[1]})
        j = r.json()
        print('Number of results: {}'.format(j.get('count')))
        for p in j.get('results'):
            print(p.get('name'))
            for furl in p.get('films'):
                f = get(furl)
                f = f.json()
                print('\t{}'.format(f.get('title')))
        while j.get('next'):
            r = get(j.get('next'))
            j = r.json()
            for p in j.get('results'):
                print(p.get('name'))
                for furl in p.get('films'):
                    f = get(furl)
                    f = f.json()
                    print('\t{}'.format(f.get('title')))

    except Exception as e:
        print(e)
