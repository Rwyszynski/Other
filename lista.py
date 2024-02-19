listaGosci = {

            ('Arkadiusz', 29, 'mężczyzna'),
            ('Piotr', 30, 'mężczyzna'),
            ('Kinga', 21, 'Kobieta')
            }

listaGosci2 = {

            ('Janusz', 21, 'mężczyzna'),
            ('Łukasz', 60, 'mężczyzna'),
            ('Kinga', 21, 'Kobieta')
            }

listaGosci3 = listaGosci and listaGosci2

for imie, wiek, plec in listaGosci3:
    print("Imie: ", imie)
    print("Wiek: ", wiek)
    print("Płeć: ", plec)
    print("\n")
