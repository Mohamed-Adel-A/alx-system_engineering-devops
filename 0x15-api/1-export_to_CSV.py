#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
- records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""

import csv
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

    todo_list = [[t.get("userId"),
                  user_data.get("username"),
                  t.get("completed"),
                  t.get("title")]
                 for t in todo_data]

    filename = "{}.csv".format(user_id)
    with open(filename, 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        write.writerows(todo_list)
