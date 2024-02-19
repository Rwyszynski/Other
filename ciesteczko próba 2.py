import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except Error:
    print("zły link")
else:
    zadaniaWykonane = dict()
    for names in tasks:
        if (names["completed"] == True):
            
            try:
                zadaniaWykonane[enames["userId"]] += 1
            except:
                zadaniaWykonane[names["userId"]] = 1

    ludzieOdZadan = []
    maksZadaniaWykonane = max(zadaniaWykonane.values())
    for userId, iloscRazy in zadaniaWykonane.items():
        if maksZadaniaWykonane == iloscRazy:
            ludzieOdZadan.append(userId)
