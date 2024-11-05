def calcular_costo_llamada(duracion, dia, turno=None):
    # Cálculo del costo base según la duración en minutos
    if duracion <= 5:
        costo_base = duracion * 1.0
    elif duracion <= 8:
        costo_base = 5 * 1.0 + (duracion - 5) * 0.80
    elif duracion <= 10:
        costo_base = 5 * 1.0 + 3 * 0.80 + (duracion - 8) * 0.70
    else:
        costo_base = 5 * 1.0 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

    # Aplicación del impuesto según el día y turno
    if dia.lower() == "domingo":
        impuesto = 0.03  # 3% si es domingo
    else:
        # Requiere especificar turno si no es domingo
        if turno.lower() == "mañana":
            impuesto = 0.15  # 15% en turno de mañana
        elif turno.lower() == "tarde":
            impuesto = 0.10  # 10% en turno de tarde
        else:
            raise ValueError("Turno no válido. Use 'mañana' o 'tarde'.")

    # Cálculo del total con el impuesto
    costo_impuesto = costo_base * impuesto
    costo_total = costo_base + costo_impuesto

    return costo_base, costo_impuesto, costo_total

# Entrada de datos
duracion = int(input("Ingrese la duración de la llamada en minutos: "))
dia = input("Ingrese el día de la llamada (por ejemplo, 'domingo' o 'otro'): ").lower()

# Si no es domingo, solicita el turno
if dia != "domingo":
    turno = input("Ingrese el turno de la llamada ('mañana' o 'tarde'): ").lower()
else:
    turno = None

# Llamada a la función y salida de resultados
costo_base, costo_impuesto, costo_total = calcular_costo_llamada(duracion, dia, turno)

print(f"Costo base de la llamada: {costo_base:.2f} euros")
print(f"Impuesto aplicado: {costo_impuesto:.2f} euros")
print(f"Costo total de la llamada: {costo_total:.2f} euros")
