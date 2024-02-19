from enum import Enum

import random

Event = Enum('Event',['Chest', 'Empty'])


eventDictionary = {
                Event.Chest: 0.6,
                Event.Empty : 0.4
                }
eventList = list(eventDictionary.keys())
eventProbability = list(eventDictionary.values())




gameLenght = 5

while gameLenght > 0:
    gameAnswer = input("czy chcesz iść")
    if (gameAnswer == "yes"):
        print("zobaczmy co masz")

        drawnEvent = random.choices(eventList, eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("wylosowałeś skrzynię")
        elif (drawnEvent == Event.Empty):  
            print("nic nie ma")
    else:
        print("nie możesz zrobić nic innego")
        continue
    
    gameLenght = gameLenght -1
