import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except Error:
    print("złe dane")
else:

    zliczanieLudzi = dict()
    for people in tasks:
        if (people["completed"] == True):
            try:
                zliczanieLudzi[people["userId"]] +=1
            except KeyError:
                zliczanieLudzi[people["userId"]] = 1

    policzenieDanych = []
    najwyzszaWartosc = max(zliczanieLudzi.values())
    for userId, wart in zliczanieLudzi.items():
        if (wart == najwyzszaWartosc):
            policzenieDanych.append(userId)    
print(policzenieDanych)
