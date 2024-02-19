x = "myszydokazujągdykotanieczują"
x = [*x]
y={}
print(x)

for i in x:
    if i in y:
        y[i] +=1
    else:
        y[i] = 1

print(y)

for key, value in y.items():
    if value == 3:
       print(key)

#for key, value in y.items():
#    print(key, value)
