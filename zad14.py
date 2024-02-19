L = [11, 22, 33, 44, 55, 66, 77, 88, 99, 1010]
s = 'a nMozh^tKysPW 9ęxi b$uML'

a = L[:5]

print(a)


b = s[slice(-1,-(len(s)+1),-2)]
print(b)
