

import time


def function_performance(func, arg, how_many=1):

    sum = 0
    for liczba in range (0, how_many):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum

kontener1 = {liczba for liczba in range(1, 10000)}
kontener2 = [liczba for liczba in range(1, 10000)]

def sprawdzanie_liczby(sprawdzana):


    
    if sprawdzana in kontener1:
        return True
    else:
        print("coś nie tak")
        return False

print(function_performance(sprawdzanie_liczby, 1000, how_many=2))

