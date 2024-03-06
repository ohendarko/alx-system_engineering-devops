#!/usr/bin/python3
"""
Contains a recursive function that parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    queries the Reddit API
    and returns a list containing the titles of all hot articles
    """
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])

            for post in children:
                title = post['data']['title'].lower()
                for word in word_list:
                    word_lower = word.lower()
                    if word_lower in title:
                        count_dict[word_lower] = count_dict.get(
                            word_lower, 0) + title.count(word_lower)
            after = data.get('after')
            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                give_results(count_dict)
        else:
            give_results(count_dict)
    except requests.RequestException as e:
        give_results(count_dict)


def give_results(count_dict):
    """
    Prints the results in descending order by count and alphabetically
    for equal counts.
    """
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")
