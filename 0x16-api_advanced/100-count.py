#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
and returns a list containing the titles of
all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def count_words(subreddit, word_list, words_count_dict=dict(), after=None):
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
        title_words_list = post_title.lower().split()
        for word in word_list:
            if word.lower() in title_words_list:
                count = len([w for w in title_words_list if w == word.lower()])
                if (words_count_dict.get(word)):
                    words_count_dict[word] += count
                else:
                    words_count_dict[word] = count

    if after:
        return count_words(subreddit, word_list, after)

    if not words_count_dict:
        print()
        return
    words_count_dict = sorted(words_count_dict.items(),
                              key=lambda x:x[1],
                              reverse=True)
    for word, count in words_count_dict.items():
        print("{}: {}".format(word, count))
