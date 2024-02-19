import time

def sumuj_do(liczba):
    suma = 0

    for liczba in range(1, liczba +1):
        suma = suma + liczba

    return suma



def function_performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

def show_message(message):
    print(message)

print(function_performance(sumuj_do, 5000))
