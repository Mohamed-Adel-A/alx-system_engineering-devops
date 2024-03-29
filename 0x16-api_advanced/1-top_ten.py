#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    API_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    response = requests.get(API_url,
                            headers={"User-Agent": "Mozilla/5.0"},
                            allow_redirects=False)
    if (response.status_code >= 300):
        print("None")
        return
    json_data = response.json()
    posts_data = json_data.get("data").get("children")
    i = 0
    for post in posts_data:
        print(post.get("data").get("title"))
        i += 1
        if i == 11:
            break
