#!/usr/bin/python3
"""Query the twitter api using the provided api key and api secret"""

if __name__ == "__main__":
    from base64 import b64encode
    from requests import get, post
    from sys import argv
    try:
        key, secret, query = argv[1:]
        credentials = ':'.join([key, secret])
        credentials = b64encode(credentials.encode()).decode('utf8')
        headers = {
            'Authorization': 'Basic {}'.format(credentials),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        data = {'grant_type': 'client_credentials'}
        p = post('https://api.twitter.com/oauth2/token',
                 headers=headers,
                 data=data)
        j = p.json()
        if j.get('token_type') == 'bearer':
            bearer = j.get('access_token')
        else:
            exit('Could not get access token')
        data = {
            'q': query,
            'count': 5
        }
        authorization = 'Bearer {}'.format(bearer)
        headers = {'Authorization': authorization}
        r = get('https://api.twitter.com/1.1/search/tweets.json',
                headers=headers,
                params=data)
        j = r.json()
        for s in j.get('statuses'):
            tweet_id = s.get('id_str')
            text = s.get('text')
            user = s.get('user').get('name')
            print('[{}] {} by {}'.format(tweet_id, text, user))
    except Exception as e:
        print(e)
