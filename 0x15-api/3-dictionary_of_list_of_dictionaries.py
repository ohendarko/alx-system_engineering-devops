#!/usr/bin/python3
"""extend Python script to export data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    Users = response.json()
    dicta = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
        user_url = url + "/todos"
        resp = requests.get(user_url)

        tasks = resp.json()
        dicta[USER_ID] = []
        for tsk in tasks:
            TASK_COMPLETED_STATUS = tsk.get('completed')
            TASK_TITLE = tsk.get('title')
            dicta[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(dicta, f)
