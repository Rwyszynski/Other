import figury

from enum import IntEnum

Menu_Figury = IntEnum("Menu_Figury", "Kwadrat, Prostokąt, Koło, Trójkąt, Trapez")

wybor = int(input("""Wybierz figurę:
1.Kwadrat
2.Prostokąt
3.Kolo
4.Trojkat
5.Trapez"""))
            

if (wybor == Menu_Figury.Kwadrat):
    a = float(input("podaj bok kwadratu"))
    print("pole kwadratu wynosi", figury.pole_kwadratu(a))
elif (wybor == Menu_Figury.Prostokąt):
    a = float(input("podaj bok kwadratu"))
    print("pole kwadratu wynosi", figury.pole_kwadratu(a))
elif (wybor == Menu_Figury.Koło):
    a = float(input("podaj bok kwadratu"))
    print("pole kwadratu wynosi", figury.pole_kwadratu(a))
elif (wybor == Menu_Figury.Trójkąt):
    a = float(input("podaj bok kwadratu"))
    print("pole kwadratu wynosi", figury.pole_kwadratu(a))
elif (wybor == Menu_Figury.Trapez):
    a = float(input("podaj bok kwadratu"))
    print("pole kwadratu wynosi", figury.pole_kwadratu(a))
