lista = []


def pierwsza(n):
    for i in range(n):
        if n % (i+1) == 0:
            lista.append(i+1)
            print("ok")
       


    
print(len(lista))
