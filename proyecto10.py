def calcular_costo_viaje(num_alumnos):
    if num_alumnos >= 100:
        costo_por_alumno = 65
        costo_total = num_alumnos * costo_por_alumno
    elif num_alumnos >= 50:
        costo_por_alumno = 70
        costo_total = num_alumnos * costo_por_alumno
    elif num_alumnos >= 30:
        costo_por_alumno = 95
        costo_total = num_alumnos * costo_por_alumno
    else:
        costo_total = 4000
        costo_por_alumno = costo_total / num_alumnos if num_alumnos > 0 else 0

    return costo_total, costo_por_alumno

# Entrada de número de alumnos
num_alumnos = int(input("Ingrese el número de alumnos que realizarán el viaje: "))
costo_total, costo_por_alumno = calcular_costo_viaje(num_alumnos)

# Salida de resultados
print(f"El costo total a pagar a la compañía de autobuses es: {costo_total} euros")
print(f"Cada alumno debe pagar: {costo_por_alumno} euros")
