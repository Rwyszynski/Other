def digital_root(n):
    lista = 0
    n = str(n)
    newN = [*n]
    for i in newN:
        lista += int(i)
    n = lista
    if n<10:
        return n
    else:
        return digital_root(n)


print(digital_root(132189))
