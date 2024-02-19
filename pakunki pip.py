import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except json.decoder.JSONDecoderError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)
    
