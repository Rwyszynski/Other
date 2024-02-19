def fizzbuzz(n):
    #a = [i+1 for i in range(n)]
    c = []
    if n > 0:
        for i in range(n):
            if (i+1) % 5 == 0 and (i+1) % 3 == 0:
                b = "FizzBuzz"
            elif (i+1) % 5 == 0:
                b = "Buzz"
            elif (i+1) % 3 == 0:
                b =  "Fizz"
            else:
                b = i+1
            c.append(b)
            
    else:
        False
            
    return list(c)
    
print(fizzbuzz(15))









