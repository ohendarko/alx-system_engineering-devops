#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her to_do list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    if not argv[1]:
        print("Usage: <file> <id>")
        exit(1)
    e_id = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{api_url}/users/{e_id}"
    todo_url = f"{user_url}/todos"

    # Getting user response
    response = requests.get(user_url).json()

    # Getting employee name
    name = response.get("name")

    # Getting todos list
    todos = requests.get(todo_url).json()
    tot_tasks = len(todos)  # number of total tasks
    incomp_tasks = sum([elem['completed'] is False for elem in todos])
    comp_tasks = tot_tasks - incomp_tasks

    print(f"Employee {name} is done with tasks({comp_tasks}/{tot_tasks})")

    for elem in todos:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
