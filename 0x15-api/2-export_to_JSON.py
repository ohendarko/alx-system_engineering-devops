#!/usr/bin/python3
"""extend Python script to export data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    USER_ID = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    response = requests.get(user_url)
    USERNAME = response.json().get('username')
    task = user_url + "/todos"
    resp = requests.get(task)
    tasks = resp.json()

    dicta = {USER_ID: []}
    for tsk in tasks:
        TASK_COMPLETED_STATUS = tsk.get('completed')
        TASK_TITLE = tsk.get('title')
        dicta[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        })

    with open(f'{USER_ID}.json', 'w') as f:
        json.dump(dicta, f)
