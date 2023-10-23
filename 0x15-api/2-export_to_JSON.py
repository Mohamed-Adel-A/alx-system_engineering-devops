#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
- records all tasks that are owned by this employee
- Format must be: { "USER_ID":
  [{"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
   {"task": "TASK_TITLE",
   "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
   ... ]}
- File name must be: USER_ID.json
"""

import json
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

    todo_list = [{"task": t.get("title"),
                  "completed": t.get("completed"),
                  "username" : user_data.get("username")}
                 for t in todo_data]

    todo_dict = dict()
    todo_dict[str(user_id)] = todo_list

    filename = "{}.json".format(user_id)
    with open(filename, 'w') as f:
        json.dump(todo_dict, f)
