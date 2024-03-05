#!/usr/bin/python3
"""
Contains a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            subscribers = data.get('subscribers', 0)
            return (subscribers)
        else:
            return (0)
    except requests.RequestException as e:
        return (0)
