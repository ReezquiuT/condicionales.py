def obtener_dias_del_mes(mes):
    # Diccionario que mapea el número del mes al número de días
    dias_por_mes = {
        1: 31,   # Enero
        2: 28,   # Febrero (no considera años bisiestos)
        3: 31,   # Marzo
        4: 30,   # Abril
        5: 31,   # Mayo
        6: 30,   # Junio
        7: 31,   # Julio
        8: 31,   # Agosto
        9: 30,   # Septiembre
        10: 31,  # Octubre
        11: 30,  # Noviembre
        12: 31   # Diciembre
    }
    
    return dias_por_mes.get(mes, "Error: Número inválido. Debe ser del 1 al 12.")

# Solicitar al usuario que ingrese un número del 1 al 12
try:
    mes_input = int(input("Ingrese un número del 1 al 12 para el mes: "))
    dias_mes = obtener_dias_del_mes(mes_input)
    print(f"El mes {mes_input} tiene {dias_mes} días.")
except ValueError:
    print("Error: Debe ingresar un número entero.")
