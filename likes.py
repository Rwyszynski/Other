def likes(names):
    lista = ""
    if len(names) == 0:
        lista += 'no one '
    elif (len(names) == 1): 
        for i in names:
            lista += (i + ' ')
    elif (len(names) == 2):
        for i in names:
            if i == 0:
                lista += (i + ', ')
            else:
                lista += i
    lista += 'likes this'
    return lista





print(likes([]))
