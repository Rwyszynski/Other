
b = 0

wynik = 0

i=0
while i < 3:
    a = int(input("podaj liczbę do dodania"))
    
    if a > 0:
        wynik += a
    else:
        continue

    i +=1
print(wynik)
