#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
- Records all tasks from all employees
- Format must be: { "USER_ID":
  [{"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
   {"task": "TASK_TITLE",
   "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
   ... ]}
- File name must be: todo_all_employees.json
"""

import json
import requests


if __name__ == "__main__":

    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(user_url)
    users_data = users_response.json()

    users_dict = dict()
    for user in users_data:
        user_id = user.get("id")
        todo_url = users_url + "/{}/todos/".format(user_id)
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        todo_list = [{"username": user_data.get("username"),
                      "task": t.get("title"),
                      "completed": t.get("completed")}
                     for t in todo_data]
    
        users_dict[str(user_id)] = todo_list

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        json.dump(users_dict, f)
