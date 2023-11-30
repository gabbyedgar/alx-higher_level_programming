#!/usr/bin/python3
"""
Get the 10 most recent commits from the repository specified on
the command line ordered most recent to oldest in the
format: `<sha>: <author name>`
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

    try:
        r = get(url)
        j = r.json()
        for commit in j[:10]:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit')
                                  .get('author')
                                  .get('name')))
    except IndexError as e:
        print(e)
