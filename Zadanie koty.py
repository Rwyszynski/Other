
try:
    with open("tekst.txt", "r", encoding="UTF-8") as file:
        koty = file.read()
        cat = koty.count("kot") 
        print(f"Jest tutat{cat} kotów")
        
except FileNotFoundError:
    print("zła nazwa pliku")
except PermissionError:
    print("Nie masz dostępu do pliku")
