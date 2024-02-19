import random


def will_weapon_hit(weapon_chance):
    hit_chance = random.uniform(0,100)
    if (weapon_chance < hit_chance):
        return "hit"
    return "not hit"

print(will_weapon_hit(50))

listHit = []

x=0
          
while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))
print(listHit)

from collections import Counter

dictioneryHit = Counter(listHit)
 
print(dictioneryHit)
