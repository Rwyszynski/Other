import random

cartList = [ "Jopek", "Jopek", "Dama", "Dama", "Król", "Król"]



random.shuffle(cartList)

print(cartList)

karty1 = []
x = 0
while x < 3:
    x = x+1
    karty1.append(cartList[-1])
    cartList.pop()
    


print(cartList)
print(karty1)
