#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import csv
import json
from requests import get
import sys

if __name__ == "__main__":
    emply_id = sys.argv[1]

    user_resp = f'https://jsonplaceholder.typicode.com/users/{emply_id}'
    to_do_resp = f'https://jsonplaceholder.typicode.com/users/{emply_id}/todos'

    usr = get(user_resp)
    todo = get(to_do_resp)

    to_pars = json.loads(todo.text)
    pars = json.loads(usr.text)

    titles = [i.get('title') for i in to_pars if i.get('completed')]
    tot = len(to_pars)
    don = len(titles)
    username = pars.get("username")

    with open("2.csv", "w") as csvfile:
        field = ['usr_id', 'usr_name', 'tsk_compltd_stats', "tsk_titl"]
        writ = csv.DictWriter(csvfile, fieldnames=field, quoting=csv.QUOTE_ALL)
        for i in to_pars:
            writ.writerow({'usr_id': str(i.get('userId')),
                           'usr_name': str(username),
                           'tsk_compltd_stats': str(i.get('completed')),
                           'tsk_titl': str(i.get('title'))})
