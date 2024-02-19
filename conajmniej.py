def znajdz_wielkie_litery(tekst):
    wielkie_litery = []
    for litera in tekst:
        if litera.isupper():
            wielkie_litery.append(litera)
    return wielkie_litery

print(znajdz_wielkie_litery('helloWorld'))
