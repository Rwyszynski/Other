

def opening(otworz):
    otworz = input("podaj nazwe pliku do otworzenia")
    
    try:
        with open(otworz, "r", encoding="UTF-8") as file:
            plik = file.readlines()
            print(plik)
    except FileNotFoundError:
        print("nie ma takiego pliku")

opening("test.txt")


