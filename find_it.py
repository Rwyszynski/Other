def find_it(seq):
    seq1 = set(seq)
    tab = []
    b = 0
    for i in seq1:
        tab.append(seq.count(i))
    seq1 = list(seq1)        
    for (x,y) in zip(tab,seq1) :
        if x % 2 != 0:
            return y




    



        





print(find_it([0,1,0,1,0]))
