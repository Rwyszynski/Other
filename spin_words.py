def spin_words(sentence):
    sentence = sentence.split(" ")
    wynik = []
    for i in sentence:
        if len(i) < 5:
            wynik.append(i)
        else:
            i = i
            i = "".join([*i][::-1])
            wynik.append(i)
    wynik = " ".join(wynik)
    return wynik



#    elif len(sentence) >= 5:
#        sentence = "".join([*sentence][::-1])










print(spin_words("This is another test"))
