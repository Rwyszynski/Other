def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a**2

def pole_kola(r):
    return 3,14 * r**2



wybor = int(input("1-pole prostokąta, 2-pole kwadratu, 3-pole koła\n"))
print("wybrałeś:", wybor)

if (wybor == 1):
    
    a = input("podaj a")
    b = int(input("podaj b"))
    pole_prostokata(a, b)
    
elif (wybor == 2):
    a = int(input("podaj a"))
    pole_kwadratu(a)
    
elif (wybor == 3):
    r = int(input("podaj r"))
    pole_kola(r)
    
