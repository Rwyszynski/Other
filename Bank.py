def addition_without_carrying(a,b):
    tablica = []
    au = list(str(a))
    bu = list(str(b))
    d = len(au)
    e = len(bu)
    o = reversed(au)
    p = reversed(bu)
    v = [int(x) for x in o]
    w = [int(y) for y in p]
    j=[]
    l =[]
    l.append(d)
    l.append(e)
    q = max(l)
    for i in range(q):
        if ((v[i])+(w[i])) < 10:

            j.append((v[i])+(w[i]))
               
        else :  
            j.append(((v[i])+(w[i]))-10)
            
                
        i += 1
    
    r = list(reversed(j))
    pol = [str(pol) for pol in r]
           
    return "".join(pol)




print(addition_without_carrying(4648, 3533))













