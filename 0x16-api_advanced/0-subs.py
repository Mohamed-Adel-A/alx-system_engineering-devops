#!/usr/bin/python3
"""
a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit.
    """
    API_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(API_url,
                            header={"User-Agent": "Mozilla/5.0"},
                            allow_redirects=False)
    if response.status_code == 404:
        return (0)
    subs_data = response.json().get("data").get("subscribers")
    return (subs_data)
