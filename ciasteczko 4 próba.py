import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except Error:
    print("zły link")
else:
    zliczanieZrobionych = dict()
    for people in tasks:
        if (people["completed"] == True):
            try:
                zliczanieZrobionych[people["userId"]] +=1
            except KeyError:
                zliczanieZrobionych[people["userId"]] = 1

    zliczanieNajwyzszych = []
    najwyzszaWartosc = max(zliczanieZrobionych.values())
    for userId, wart in zliczanieZrobionych.items():
        if (wart == najwyzszaWartosc):
            zliczanieNajwyzszych.append(userId)
    print(userId)
