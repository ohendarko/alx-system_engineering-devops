#!/usr/bin/python3
"""extend Python script to export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    response = requests.get(user_url)
    username = response.json().get('username')
    task = user_url + "/todos"
    resp = requests.get(task)
    tasks = resp.json()

    with open(f"{user_id}.csv", 'w') as csvfile:
        for task in tasks:
            comp = task.get('completed')
            title = task.get('title')
            csvfile.write(f'"{user_id}","{username}","{comp}","{title}"\n')
