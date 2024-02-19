def high(x):
    splited = x.split(" ")
    wyr = []
    liss = []
    lista ='abcdefghijklmnopqrstuvwxyz'
    lista = list(str(lista))
    for word in splited:
        wyr.append(list(str(word)))
        for i in word:
            a = (lista.index(i)+1)
            

            liss.append(a)
    print(liss)















print(high('man i need a taxi up to ubud'))
