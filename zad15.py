a = "python_moj_kod.py"
b = "python_notatki.txt"

c = a[slice(6)]

def sprawdzanie(arg):
    if arg[slice(6)] == 'python' and arg[slice(-1,-4,-1)] == "yp.":
        return "Prawda"

print(sprawdzanie(a))
    
print(a[slice(-1,-4,-1)])
