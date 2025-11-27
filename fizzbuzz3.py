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

# def fizzBuzz(n):
#     # Inicializamos una variable para almacenar el resultado completo
#     # como un solo string, agregando cada línea con \n
#     resultado = ""

#     # Usamos un loop desde 1 hasta n (incluyendo n)
#     for i in range(1, n + 1):

#         # Si el número es múltiplo de 3 y 5, agregamos "FizzBuzz"
#         if i % 3 == 0 and i % 5 == 0:
#             resultado += "FizzBuzz\n"

#         # Si solo es múltiplo de 3, agregamos "Fizz"
#         elif i % 3 == 0:
#             resultado += "Fizz\n"

#         # Si solo es múltiplo de 5, agregamos "Buzz"
#         elif i % 5 == 0:
#             resultado += "Buzz\n"

#         # Si no es múltiplo de ninguno, agregamos el número como texto
#         else:
#             resultado += str(i) + "\n"

#     # Devolvemos el string final con todas las líneas del resultado
#     return resultado

# # Convertimos la entrada del usuario en un entero
# n = int(input())

# # Llamamos a fizzBuzz y mostramos el resultado
# print(fizzBuzz(n))