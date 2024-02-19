#!/usr/bin/python3
"""
using this REST API, for a given user ID
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    # Accept the user Id from the command line arguments
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.json".format(user_id), "w", newline="") as jsonfile:
        json.dump({user_id: [{
            "task": t.get('title'),
            "completed": t.get("completed"),
            "username": username} for t in todos]}, jsonfile)
