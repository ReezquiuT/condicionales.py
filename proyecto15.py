def obtener_resultado(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "tijera" and jugador2 == "papel") or \
         (jugador1 == "papel" and jugador2 == "piedra"):
        return "Gana Jugador 1"
    else:
        return "Gana Jugador 2"

# Solicitar las opciones de los jugadores
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Opciones válidas
opciones_validas = ["piedra", "papel", "tijera"]

# Verificar si las opciones son válidas
if jugador1 not in opciones_validas:
    print("Opción incorrecta para Jugador 1. Debe ser 'piedra', 'papel' o 'tijera'.")
elif jugador2 not in opciones_validas:
    print("Opción incorrecta para Jugador 2. Debe ser 'piedra', 'papel' o 'tijera'.")
else:
    # Obtener y mostrar el resultado
    resultado = obtener_resultado(jugador1, jugador2)
    print(resultado)
