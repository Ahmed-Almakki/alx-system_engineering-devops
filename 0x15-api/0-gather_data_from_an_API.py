#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
from requests import get
import json
import sys


employ_id = sys.argv[1]

user_resp = f'https://jsonplaceholder.typicode.com/users/{employ_id}'
to_do_resp = f'https://jsonplaceholder.typicode.com/users/{employ_id}/todos'

usr = get(user_resp)
todo = get(to_do_resp)

to_pars = json.loads(todo.text)
pars = json.loads(usr.text)

name = pars.get('name')
titles = [i['title'] for i in to_pars if i['completed']]
tot = len(to_pars)
don = len(titles)
print("Employee {} is done with tasks({}/{}):".format(name, don, tot))
for t in titles:
    print("     {}".format(t))
