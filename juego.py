import random

def pedir_rango():
    while True:
        try:
            minimo = int(input("Número mínimo: "))
            maximo = int(input("Número máximo: "))
            if minimo < maximo:
                return minimo, maximo
            else:
                print("⚠️ Mínimo debe ser menor que máximo. Intenta de nuevo.")
        except ValueError:
            print("⚠️ Ingresa valores numéricos válidos. Ejemplo: 1 y 100.")

def juego_adivinanza(rango=(1, 100)):
    numero_secreto = random.randint(rango[0], rango[1])
    intentos = 0
    adivinanza = None

    print("\n--- ¡Bienvenido al Juego de Adivinanza! ---")
    print(f"He pensado un número entre {rango[0]} y {rango[1]}.")
    print("¡Intenta adivinarlo! (Escribe 'salir' para abandonar el juego)\n")

    while adivinanza != numero_secreto:
        entrada = input("Introduce tu número: ")
        if entrada.lower() == 'salir':
            print("👋 ¡Gracias por jugar! ¡Hasta pronto!")
            return intentos
        try:
            adivinanza = int(entrada)
            intentos += 1

            if adivinanza < numero_secreto:
                print("🔽 Demasiado bajo. ¡Intenta de nuevo!")
            elif adivinanza > numero_secreto:
                print("🔼 Demasiado alto. ¡Intenta de nuevo!")
            else:
                print(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("⚠️ Error: Ingresa un número válido o 'salir'.")
    return intentos

def main():
    record_intentos = None
    while True:
        print("\n¿Quieres personalizar el rango? (s/n): ", end="")
        op = input().strip().lower()
        rango = (1, 100)
        if op == "s":
            rango = pedir_rango()

        intentos = juego_adivinanza(rango)
        if intentos and (record_intentos is None or intentos < record_intentos):
            record_intentos = intentos
            print(f"🏅 ¡Nuevo récord! ¡Lo lograste en {intentos} intentos!")

        jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if jugar_otra != "s":
            print("👋 ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
