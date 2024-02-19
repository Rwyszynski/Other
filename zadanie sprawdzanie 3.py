import time



def sprawdzanie(func, how_many=1, **arg ):
    sum = 0
    
    for liczba in range(1, how_many):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum


koszyk1 = [liczba for liczba in range(1000)]
koszyk2 = {liczba for liczba in range(1000)}


def spr(wartosc, container):
    if wartosc in container:
        return True
    else:
        return False

print(sprawdzanie(spr, 50000, wartosc=100, container=koszyk1 ))
print(sprawdzanie(spr, 50000, wartosc=100, container=koszyk2 ))
