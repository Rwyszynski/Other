

import random

from enum import Enum

Event = Enum("Event", ["Chest", "Empty"])

eventDictionary = {Event.Chest: 0.6,
                   Event.Empty: 0.4
                }

eventList = list(eventDictionary.keys())
eventProbability = list(eventDictionary.values())



gameLenght = 5

while gameLenght > 0:
    gameAnswer = input("Do you want to play")
    if (gameAnswer == 'yes'):
        print("ok co tam masz")
        drawnEvent = random.choices(eventList,eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("wylosowałes skrzynię")
        elif (drawnEvent == Event.Empty):
            print("nie ma nic")
    else:
        print("oj źle")
        continue

    
    gameLenght = gameLenght -1
