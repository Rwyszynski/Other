def order(sentence):
    ordered = []
    sentence = sentence.split(" ")
    a = 1
    for i in range(len(sentence)):
        
        if str(a) in sentence[i]:
            a+=1
            ordered.append(sentence[i])

    if len(ordered) == len(sentence):
        return ordered
    else:
        return order(sentence)


print(order("4of Fo1r pe6ople g3ood th5e the2"))
