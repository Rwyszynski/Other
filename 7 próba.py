import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except Error:
    print("nie da się")
else:
    listaNajwiekszych = dict()
    for zadania in tasks:
        if (zadania["completed"] == True):
            try:
                listaNajwiekszych[zadania["userId"]] +=1
            except KeyError:
                listaNajwiekszych[zadania["userId"]] =1

    tablicaNajwiekszych = []
    MaksWart = max(listaNajwiekszych.values())
    for userId, ludzie in listaNajwiekszych.items():
        if (ludzie == MaksWart):
            tablicaNajwiekszych.append(userId)


