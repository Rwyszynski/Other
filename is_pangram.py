def is_pangram(s):
    s = (str(list(s))).lower()
    z = 'abcdefghijklmnopqrstuvwxyz'
    z = str(list(z))
    tab = []
    for y in z:
        if y in s:

            print(s)

            continue
        else:
            return False
    return True







print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))
