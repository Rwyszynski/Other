lista = [1, 2, 3, 4, 5, 6,]

potega = []

parzyste = []

for element in lista:
    potega.append(element**2)

for element in lista:
    if (element % 2 == 0):
        parzyste.append(element)
    
