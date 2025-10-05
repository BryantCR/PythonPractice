def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")

    for i in range(0, 13):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(tabla_multiplicar(numero))
