#!/usr/bin/python3
""" query subscribers on a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """ Return the numbers of subreddit subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": 'Mozilla/5.0'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except requests.RequestException:
        return 0
