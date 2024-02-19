import time



def sprawdzanie(func, arg, how_many=1):
    sum = 0
    
    for liczba in range(1, how_many):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum


koszyk1 = [liczba for liczba in range(1000)]
koszyk2 = {liczba for liczba in range(1000)}


def spr(wartosc):
    if wartosc in koszyk1:
        return True
    else:
        return False

print(sprawdzanie(spr, 450, how_many=100))
