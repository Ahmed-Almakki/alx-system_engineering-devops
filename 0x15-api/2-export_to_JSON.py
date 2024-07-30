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

    ar = []
    for i in to_pars:
        dictt = {}
        dictt['task'] = i.get('title')
        dictt['completed'] = i.get('completed')
        dictt['username'] = username
        ar.append(dictt)
    dic = {pars.get('id'): ar}
    with open('2.json', 'w') as json_file:
        json.dump(dic, json_file)
