# Solicitar la base y el exponente al usuario
base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

# Calcular la potencia según el valor del exponente
if exponente > 0:
    resultado = base ** exponente
    print("El resultado es:", resultado)
elif exponente == 0:
    resultado = 1
    print("El resultado es:", resultado)
else:
    resultado = 1 / (base ** abs(exponente))
    print("El resultado es:", resultado)
