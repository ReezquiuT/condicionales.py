# Solicitar dos números al usuario
numerador = float(input("Ingresa el primer número (numerador): "))
denominador = float(input("Ingresa el segundo número (denominador): "))

# Comprobar si el denominador es cero
if denominador != 0:
    resultado = numerador / denominador
    print("El resultado de la división es:", resultado)
else:
    print("No se puede dividir entre cero. Por favor, ingresa un denominador distinto de cero.")
