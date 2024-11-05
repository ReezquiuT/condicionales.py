def obtener_dia_semana(dia):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    
    return dias.get(dia, "Error: Número inválido. Debe ser del 1 al 7.")

# Solicitar al usuario que ingrese un número del 1 al 7
try:
    dia_input = int(input("Ingrese un número del 1 al 7 para el día de la semana: "))
    dia_semana = obtener_dia_semana(dia_input)
    print(dia_semana)
except ValueError:
    print("Error: Debe ingresar un número entero.")
