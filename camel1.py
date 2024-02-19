def solution(s):
    lista = [*s]
    malaLista = s.lower()
    malaLista2 = [*malaLista]
    for i in zip(lista, malaLista):
        if (str(lista[i]) != str(malaLista2[i])):
            print(lista[i])
    print(lista)
    print(malaLista2)


print(solution("breakCamelCase"))
