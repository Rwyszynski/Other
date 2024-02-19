def odd_or_even(arr):
    suma = sum(arr)
    if suma % 2 == 0:
        return "even"
    else:
        return "odd"




print(odd_or_even([0, 2, 2]))
