#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = user_url + "/todos/"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    completed_todo = [todo.get("title")
                      for todo in todo_data
                      if todo.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(user_data.get("name"),
                  len(completed_todo),
                  len(todo_data)))

    for title in completed_todo:
        print("\t {}".format(title))
