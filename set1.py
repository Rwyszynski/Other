A = [1,2,3,3,2,1,2,3]
B = []

for a in A:
    if a not in B:
        B.append(a)

print(B)
