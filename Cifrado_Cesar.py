print("1.Cifrar\n2.Descifrar")
opcion = int(input("Ingrese la opcion: "))
Frase = input("Ingrese la frase a cifrar: ")

def Cifrado():
    Frase_cifrada = ""
    for i in Frase:
        if i == " ":
            Frase_cifrada += " "
        else:
            Frase_cifrada += chr(ord(i) + 3)
    return Frase_cifrada

def Descifrado():
    Frase_descifrada = ""
    for i in Frase:
        if i == " ":
            Frase_descifrada += " "
        else:
            Frase_descifrada += chr(ord(i) - 3)
    return Frase_descifrada

if opcion == 1:
    print(Cifrado())
elif opcion == 2:
    print(Descifrado())
