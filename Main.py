print("Witaj w narzędziu do dekodowania i kodowania szyfru Cezara!")
print("Moliwe tryby działania:")
print()
print("1. Szyfrowanie")
print("2. Deszyfrowanie")

mode = int(input("Wybierz tryb pracy narzędzia: "))

match mode:
    case 1: 
        print()
