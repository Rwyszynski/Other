def persistence(n):
    licznik = 0
    mnoz = 1
    while n >= 10:
        multi_dig = [(int(i)) for i in str(n)]
        for i in multi_dig:
            mnoz = mnoz *i
        licznik += 1
        
        n = mnoz
        mnoz = 1

    return licznik





print(persistence(39))





