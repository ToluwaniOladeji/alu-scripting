#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    of a given subreddit. If not valid, prints None.
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python:top.ten:v1.0 (by /u/YourUsername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)

