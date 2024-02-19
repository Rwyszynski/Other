def tower_builder(n_floors):
    lista = []
    a = n_floors
    i = 0
    j = 1
    while i < (n_floors):
        a-=1
        lista.append(a*' '+j*'*'+a*' ')
        i+=1
        j+=2
    return lista
    


print(tower_builder(6))
