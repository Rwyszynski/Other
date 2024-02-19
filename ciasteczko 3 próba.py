import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except Error:
    print("podales zly link")
else:
    zliczanieLudzi = dict()
    for ludzie in tasks:
        if (ludzie["completed"] == True):
            try:
                zliczanieLudzi[ludzie["userId"]] +=1
            except KeyError:
                zliczanieLudzi[ludzie["userId"]] = 1

    tablicaDoIlosci = []            
    maksWartosc = max(zliczanieLudzi.values())        
    for userId, wartosc in zliczanieLudzi.items():
        if maksWartosc == wartosc:
            tablicaDoIlosci.append(userId)

