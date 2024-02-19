
lista =[]

for element in range(2,470):
    if (element % 7 ==0) and not (element % 5 ==0):
        lista.append(element)
print(lista)
