# Solicitar una cadena al usuario
caracter = input("Ingresa un carácter: ")

# Comprobar si es una letra mayúscula
if len(caracter) == 1 and caracter.isalpha() and caracter.isupper():
    print("Es una letra mayúscula")
else:
    print("No es una letra mayúscula")
