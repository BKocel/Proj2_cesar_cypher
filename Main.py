# Encrypting function
def encrypt(shift, text):
    i = 0
    encrypted= []
    inter1 = []
    inter2 = []
    while i in range(len(text)):
        inter1.append(ord(text[i]))
        if inter1[i] + shift > 122:
            shift2 = inter1[i] - 122
            inter2.append(96 +shift + shift2)
        elif inter1[i] < 97:
            inter2.append(inter1[i])
        elif inter1[i] > 122:
            inter2.append(inter1[i])
        else:
            inter2.append(inter1[i]+shift)
        encrypted.append(chr(inter2[i]))
        i+=1
    return(encrypted)
    # print(* inter1, sep=";") # DEBUG only
    # print(* inter2, sep=";") # DEBUG only
    # print(* encrypted, sep=";") # DEBUG only
    
    

# Decrypting function
def decrypt(shift, text):
    i = 0
    decrypted= []
    inter1 = []
    inter2 = []
    while i in range(len(text)):
        inter1.append(ord(text[i]))
        if inter1[i] == 97:
            inter2.append(122 - shift)
        elif inter1[i] < 97:
            inter2.append(inter1[i])
        elif inter1[i] > 122:
            inter2.append(inter1[i])
        else:
            inter2.append(inter1[i]-shift)
        decrypted.append(chr(inter2[i]))
        i+=1
    return(decrypted)
    # print(* inter1, sep=";") # DEBUG only
    # print(* inter2, sep=";") # DEBUG only
    # print(* decrypted, sep=";") # DEBUG only
    # print("Function Called") # for DEBUG only


# Input text to list function
def txlist(text):
    i = 0
    out = []
    while i in range(len(text)) :
        out.append(text[i])
        i+= 1
    #print(out) # DEBUG only
    return(out)

# Output list to text function
def listtx(list):
    out = ''.join(str(x) for x in list)
    return(out)

# CLI
print("Witaj w narzędziu do dekodowania i kodowania szyfru Cezara!")
text = txlist(input("Podaj tekst do odszyfrowania: ").lower())
print()
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
            print(listtx(encrypt(lettershft, text)))
    case 2:
        lettershft = int(input("Podaj przesunięcie(klucz) zaszyfrowanej wiadomości (Podanie 0 spowoduje, ze program będzie deszyfrował w z przesunięciami 1-26): "))
        if lettershft <0: # incorrect lettershift handler
            print("Nieoprawna wartość, spróbój ponownie! ") 
        elif lettershft == 0: # No shift decrypt
            i = 1
            
            while i in range(1,27):
                print("Rrzesunięcie: " + str(i))
                print("Odszyfrowana wiadomość" +listtx(decrypt(i, text)))
                i+= 1
        else: # Default option
            print(listtx(decrypt(lettershft, text)))
    case _: # Unexpected value handler
        print("Niepoprawna wartość, proszę spróbować ponownie")