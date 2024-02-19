from collections import Counter
import random

kolory = ['zielony', 'czerwony', 'fioletowy', 'czarny']


print(Counter(random.choices(kolory, [1, 3, 5, 10], k=10)))
