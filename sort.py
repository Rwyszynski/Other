def flip(d, a):
    if d == 'R':
        a.sort()
        return a
    else:
        a.sort(reverse = True)
        return a

print(flip('L', [3, 2, 1, 2]))
