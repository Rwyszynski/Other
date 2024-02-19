a = 'annfa'
sprawdzanie = []

b =[*a]

print(b)

c = list(reversed(b))

print(c)

for znak1, znak2 in zip(b, c):
    if znak1 != znak2:
        sprawdzanie.append(False)

print(sprawdzanie)

if False in sprawdzanie:
    print("To nie palindrom")

