#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
and returns a list containing the titles of
all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    a recursive function that queries the Reddit API
    and returns a list containing the titles of
    all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    if not after:
        API_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        params = {
            "limit": 100
        }
        response = requests.get(API_url,
                                headers={"User-Agent": "Mozilla/5.0"},
                                params=params,
                                allow_redirects=False)
    else:
        API_url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
        params = {
            "after": after,
            "limit": 100
        }
        response = requests.get(API_url,
                                headers={"User-Agent": "Mozilla/5.0"},
                                params=params,
                                allow_redirects=False)
    if (response.status_code == 404):
        return None
    json_data = (response.json()).get("data")
    after = json_data.get("after")
    posts_data = json_data.get("children")
    for post in posts_data:
        post_title = post.get("data").get("title")
        hot_list.append(post_title)
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
