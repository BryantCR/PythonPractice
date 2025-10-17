def primo(numero):
    if numero < 2:
        return "No es primo"
    elif numero == 2:
        return "Es primo"
    for i in range(2, int(numero ** 0.5) + 1):
        print("Este es i: " + str(i))
        print("Este es numero: " + str(numero))
        if numero % i == 0:
            print("Este es numero en if: " + str(numero))
            return "No es primo"
    return "Es primo"

numero = int(input("Ingrese un número para verificar si es primo: "))
print(primo(numero))