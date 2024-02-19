slownik = {"slowo"}

print("wybierz opcję 1-dodaj definicję, 2-szukaj definicję, 3-usun definicje")

wybor = input("podaj co chcesz zrobić")


if (wybor == "1"):
    klucz = input("podaj klucz")
    definicja = input("podaj definicję")
    slownik[klucz] = definicja
elif (wybor =="2"):
    klucz = input("podaj klucz")
    if klucz in slownik:
    
        print(klucz)
        
    
