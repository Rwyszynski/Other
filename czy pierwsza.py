def czy_pierwsza(liczba):
    zakres = int(liczba/2)+1
    for x in range(100,zakres,2):
       if liczba % x == 0:
           return False
    return "prawda"
print(czy_pierwsza(345))
        
