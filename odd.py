lista = []

def odd_not_prime(n):
    if n % 2 != 0:
        for i in range(n):
            if n % (i+1) == 0:
                lista.append(i+1)
    
    else:
        return "Parzysta"
    return len(lista)








print(odd_not_prime(5))
print(lista)
