def sort_array(source_array):
    nowe = []
    odd = []
    for i in source_array:
        if i % 2 == 1:
            odd.append(i)
    odd.sort()

    for i in source_array:
        if i % 2 == 1:

            nowe.append(odd[0])
            odd.pop(0)
        else:
            nowe.append(i)
            
    return nowe







print(sort_array([5, 8, 6, 3, 4]))
