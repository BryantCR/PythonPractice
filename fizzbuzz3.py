def check(range1, range2):
    resultado = ""
    for i in range(range1, range2 + 1):
        if i % 3 == 0 and i % 5 == 0:
            resultado += "FizzBuzz\n"
        elif i % 3 == 0:
            resultado += "Fizz\n"
        elif i % 5 == 0:
            resultado += "Buzz\n"
        else:
            resultado += f"{i}\n"
    return resultado

range1 = int(input("Ingrese el primer número del rango: "))
range2 = int(input("Ingrese el segundo número del rango: "))

print(f"Resultados de FizzBuzz desde {range1} hasta {range2}:\n{check(range1, range2)}")