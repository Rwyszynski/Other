import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except Error:
    print("zły kod")
else:
    listaLudzi = dict()
    for person in tasks:
        if (person["completed"] == True):
            try:
                listaLudzi[person["userId"]] += 1
            except KeyError:
                listaLudzi[person["userId"]] = 1


    maksymalnaIloscZadan = max(listaLudzi.values())
    for user, iloscZadan in listaLudzi.items():
        if (iloscZadan == maksymalnaIloscZadan):
            print(user)



    
