#!/usr/bin/python3
"""
Contains a recursive function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API
    and returns a list containing the titles of all hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'Custom User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return hot_list
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        return recurse(subreddit, hot_list, after)
    elif response.status_code == 404:
        return None
    else:
        print('None')
