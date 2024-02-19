liczby = []

for element in range(101, 471):
    if (element % 5 == 0) and (element % 7 == 0):
        liczby.append(element)
print(liczby)
