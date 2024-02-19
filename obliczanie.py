import figury

wybor = input("""Wybierz funfcję
1.Kwadrat
2.Prostokat
3.Koło
4.Trójkąt
5.Trapez""")

if (wybor == '1'):
    a = float(input("podaj bok"))
    print("pole kwadratu wynosi",figury.pole_kwadratu(a))
