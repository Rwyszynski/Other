def persistence(n):
    suma = 0
    licznik = 0
    rozdziel = list(str(n))
    rozdziel = [int(i) for i in rozdziel]
    while rozdziel < 10 :
        mnoz = 1
        rozdziel = list(str(rozdziel))
        rozdziel = [int(i) for i in rozdziel]
        for i in rozdziel:
            mnoz = mnoz * i
        rozdziel = mnoz
        suma += mnoz
        licznik += 1
        
    
        return rozdziel



print(persistence(999))
 
