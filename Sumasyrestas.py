# Script de sumas y restas en Python con comentarios explicativos

# Definimos una función para sumar dos números
def sumar(a, b):
    """
    Recibe dos números (a y b) y devuelve su suma.
    """
    return a + b

# Definimos una función para restar dos números
def restar(a, b):
    """
    Recibe dos números (a y b) y devuelve la resta (a - b).
    """
    return a - b


# ------------------ PROGRAMA PRINCIPAL ------------------

print("=== Calculadora de Sumas y Restas ===")  # Mensaje inicial

# Usamos un ciclo while para repetir el menú hasta que el usuario quiera salir
while True:
    # Mostramos las opciones disponibles
    print("\nOpciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    # Pedimos al usuario que elija una opción
    opcion = input("Elige una opción (1/2/3): ")

    # Caso: si elige "3", termina el programa
    if opcion == "3":
        print("¡Hasta luego!")  
        break  # Sale del bucle while y termina el programa
    
    # Caso: si elige "1" o "2", pedimos los números
    elif opcion in ("1", "2"):
        try:
            # Pedimos dos números y los convertimos a tipo float (para aceptar decimales también)
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            # Si elige "1", llamamos a la función sumar()
            if opcion == "1":
                resultado = sumar(num1, num2)  # usamos la función
                print(f"Resultado: {num1} + {num2} = {resultado}")

            # Si elige "2", llamamos a la función restar()
            else:
                resultado = restar(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")

        # Si el usuario ingresa algo que no es número, mostramos un error
        except ValueError:
            print("⚠️ Error: Por favor ingresa solo números.")

    # Caso: si escribe algo distinto de 1, 2 o 3
    else:
        print("⚠️ Opción inválida, intenta de nuevo.")
