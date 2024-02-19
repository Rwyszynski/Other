def nb_year(p0, percent, aug, p):
    sum = p0
    i = 0
    while sum <= p:
        i +=1
        sum += (sum * 0.01 * percent) + (aug)
    return i

print(nb_year(1500000, 2.5, 10000, 2000000))
