import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except Error:
    print("zły link")
else:
    zliczanieMaksa = dict()
    for people in tasks:
        if (people["completed"] == True):
            try:
                zliczanieMaksa[people["userId"]] += 1
            except KeyError:
                zliczanieMaksa[people["userId"]] = 1

    tablicaNajwyzszych =[]
    maksymalnaWarotsc = max(zliczanieMaksa.values())
    for userId, wartosc in zliczanieMaksa.items():
        if (wartosc == maksymalnaWarotsc):
            tablicaNajwyzszych.append(userId)
            
            
