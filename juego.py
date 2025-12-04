# JUEGO MEJORADO: ADIVINANZA
import random
import os

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_SUPPORT = True
except ImportError:
    COLOR_SUPPORT = False

def colorize(msg, color):
    if COLOR_SUPPORT:
        return color + msg + Style.RESET_ALL
    return msg

def pedir_rango():
    """Solicita y valida un rango de números para el juego"""
    while True:
        try:
            minimo = int(input(colorize("Número mínimo: ", Fore.YELLOW)))
            maximo = int(input(colorize("Número máximo: ", Fore.YELLOW)))
            if minimo < maximo and maximo - minimo >= 5:
                return minimo, maximo
            else:
                print(colorize("⚠️ El mínimo debe ser MENOR que el máximo y la diferencia al menos 5.", Fore.RED))
        except ValueError:
            print(colorize("⚠️ Ingresa números válidos.", Fore.RED))

def pedir_limite():
    """Pregunta si se desea limitar intentos y retorna el límite"""
    while True:
        resp = input(colorize("¿Quieres limitar los intentos? (s/n): ", Fore.CYAN)).strip().lower()
        if resp == "s":
            try:
                limite = int(input(colorize("¿Cuántos intentos máximos?: ", Fore.YELLOW)))
                if limite > 0:
                    return limite
                else:
                    print(colorize("Debe ser mayor que cero.", Fore.RED))
            except ValueError:
                print(colorize("⚠️ Ingresa un número válido.", Fore.RED))
        elif resp == "n":
            return None

def juego_adivinanza(rango=(1, 100), limite_intentos=None):
    """Núcleo del juego de adivinanza"""
    numero_secreto = random.randint(*rango)
    intentos = 0
    print(colorize(f"\n💡 He pensado un número entre {rango[0]} y {rango[1]}.", Fore.MAGENTA))
    print(colorize("¡Intenta adivinarlo! (Escribe 'salir' para abandonar el juego)", Fore.CYAN))
    if limite_intentos:
        print(colorize(f"Tienes {limite_intentos} intentos como máximo.", Fore.YELLOW))
    while True:
        entrada = input(colorize("Introduce tu número: ", Fore.GREEN))
        if entrada.lower() == "salir":
            print(colorize("👋 ¡Gracias por jugar!", Fore.BLUE))
            return None
        try:
            adivinanza = int(entrada)
            intentos += 1
            if adivinanza < numero_secreto:
                print(colorize("🔽 Demasiado bajo.", Fore.RED))
            elif adivinanza > numero_secreto:
                print(colorize("🔼 Demasiado alto.", Fore.RED))
            else:
                print(colorize(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos.", Fore.GREEN))
                return intentos
            if limite_intentos and intentos >= limite_intentos:
                print(colorize(f"😮 ¡Se acabaron los intentos! El número era {numero_secreto}.", Fore.RED))
                return intentos
        except ValueError:
            print(colorize("⚠️ Ingresa un número válido o 'salir'.", Fore.RED))

def cargar_record(rango):
    """Carga el récord guardado en archivo"""
    archivo = f"record_{rango[0]}_{rango[1]}.txt"
    if os.path.exists(archivo):
        try:
            with open(archivo, "r") as f:
                return int(f.read())
        except Exception:
            return None
    return None

def guardar_record(rango, intentos):
    """Guarda el récord en archivo por rango"""
    archivo = f"record_{rango[0]}_{rango[1]}.txt"
    with open(archivo, "w") as f:
        f.write(str(intentos))

def main():
    print(colorize(
        "\n--- 🧩 Juego de Adivinanza Mejorado 🧩 ---", Fore.BLUE))
    while True:
        if input(colorize("\n¿Quieres personalizar el rango? (s/n): ", Fore.YELLOW)).strip().lower() == "s":
            rango = pedir_rango()
        else:
            rango = (1, 100)
        limite = pedir_limite()
        record_intentos = cargar_record(rango)
        intentos = juego_adivinanza(rango, limite)
        if intentos is not None:
            if record_intentos is None or intentos < record_intentos:
                guardar_record(rango, intentos)
                print(colorize(f"🏅 ¡Nuevo récord de {intentos} intentos!", Fore.GREEN))
            else:
                print(colorize(f"🥈 Récord actual: {record_intentos} intentos.", Fore.MAGENTA))
        jugar_otra = input(colorize("\n¿Quieres jugar otra vez? (s/n): ", Fore.CYAN)).strip().lower()
        if jugar_otra != "s":
            print(colorize("👋 ¡Hasta la próxima!", Fore.BLUE))
            break

if __name__ == "__main__":
    main()
