# Encrypting function
def encrypt(shift):
    print("Function Called")

# Decrypting function
def decrypt(shift):
    print("Function Called")

# CLI
print("Witaj w narzędziu do dekodowania i kodowania szyfru Cezara!")
print("Moliwe tryby działania:")
print()
print("1. Szyfrowanie")
print("2. Deszyfrowanie")

mode = int(input("Wybierz tryb pracy narzędzia: "))

match mode:
    case 1: 
        print()
        lettershft = int(input("Podaj przesunięcie(klucz) zaszyfrowanej wiadomości "))
        if lettershft <= 0: # Incorrect lettershift number
            print("Nieoprawna wartość, spróbój ponownie! ")
        else:
            encrypt(lettershft)
    case 2:
        lettershft = int(input("Podaj przesunięcie(klucz) zaszyfrowanej wiadomości (Podanie 0 spowoduje, ze program będzie deszyfrował w z przesunięciami 1-26)"))
        if lettershft <0: # incorrect lettershift handler
            print("Nieoprawna wartość, spróbój ponownie! ") 
        elif lettershft == 0: # No shift decrypt
            i = 1
            while i in range(1,27):
                decrypt(i)
                i+= 1
        else:
            decrypt(lettershft)
    case _: # Unexpected value handler
        print("Niepoprawna wartość, proszę spróbować ponownie")