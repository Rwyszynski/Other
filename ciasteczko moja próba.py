import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] +=1
            except:
                completedTaskFrequencyByUser[entry["userId"]] = 1
    
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompltedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            use
