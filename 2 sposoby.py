

def sumowanie(liczba):
    wynik = 0
    
    for liczba in range(1,liczba):
        wynik += liczba
        
    return wynik

print(sumowanie(6))

def sumowanie2(liczba):
    return sum(liczba for liczba in range(1,liczba))

print(sumowanie2(6))
