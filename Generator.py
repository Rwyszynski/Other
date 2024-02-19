
generator = ( element for element in range(400) if (element % 2 == 0))

for element in generator:
    print(element)
