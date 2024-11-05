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

   
