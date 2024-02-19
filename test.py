import random

def weapon_funkcja(weapon_check):
    
    if weapon_check > random.uniform(0,100):
        return "wieksza"
    return "mniejsza"


x = 0

listHit = []

while x < 100:
    x = x+1
    listHit.append(weapon_funkcja(50))

print(listHit)

from collections import Counter

wartosc = Counter(listHit)

print(wartosc)
