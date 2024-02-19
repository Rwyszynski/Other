def palindrome(num):
    sprawdzanie = list(str(num))
    odwrocona = sprawdzanie[::-1]
    if type(num) is str:
        return "Not Valid"
        
    elif num<0:
        return "Not Valid"
    elif sprawdzanie == odwrocona:
        return True
    else:
        return False

         
print(palindrome("asa"))
