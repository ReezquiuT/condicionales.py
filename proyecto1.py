#indica que numero es mayor si ambos numeros son iguales que ponga iguales#
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Comparar los números
if numero1 > numero2:
    print("El número mayor es:", numero1)
elif numero2 > numero1:
    print("El número mayor es:", numero2)
else:
    print("son iguales")