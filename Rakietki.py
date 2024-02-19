from random import randint

class Rocket:
    def __init__(self):
        self.altitude = 0
    def moveUp(self):
        self.altitude += 1

Rockets = [Rocket() for i in range(5)]

for i in range(10):
    randDigit = randint(0,4)
    Rockets[randDigit].moveUp()

for Rocket in Rockets:
    print(Rocket.altitude)
