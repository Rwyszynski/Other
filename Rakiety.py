from random import randint
class Rocket:
    def __init__(self):
        self.Attitude = 0

    def moveUp(self):
        self.Attitude +=1

Rakiety =[Rocket() for i in range(5)]

for i in range(10):
    rocketIndexToMove = randint(0, 4)
    Rakiety[rocketIndexToMove].moveUp()


for Rocket in Rakiety:
    print(Rocket.Attitude)
