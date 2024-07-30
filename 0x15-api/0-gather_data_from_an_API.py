#!/usr/bin/python3
"""This Script will fetch a user's todo list"""
import requests
import sys

if __name__ == "__main__":
    entrypoint = "https://jsonplaceholder.typicode.com"
    usrId = sys.argv[1]
    try:
        req_user = requests.get(
            "{ep}/users/{usrId}".format(ep=entrypoint, usrId=usrId)
        ).json()
        if req_user:
            tasks = requests.get(
                "{ep}/todos".format(ep=entrypoint),
                params={"userId": usrId}
            ).json()
            num_tasks = len(tasks)
            fin_tasks = [t for t in tasks if t['completed'] is True]
            print(
                "Employee {} is done with tasks({}/{}):"
                .format(req_user['name'], len(fin_tasks), num_tasks)
            )
            [print('\t ' + task['title']) for task in fin_tasks]
    except Exception as e:
        print(e)

