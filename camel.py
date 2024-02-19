 
def solution(s):
    lista = []
    lista2 = []
    popLista = []
    lista5 = []
    for litera in s:
        if litera.isupper():
            lista.append(s.index(litera))
    for i in lista:
        lista2.append(s[i])

    for i in len(lista2):
        lista5 = s.split(lista2[i])
    #popLista.append()
 
    print(lista2)
    print(lista5)


      



print(solution("helloWorldYeah"))
