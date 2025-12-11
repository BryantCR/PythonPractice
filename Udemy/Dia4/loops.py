list = ["a", "b", "c", "d"]

for item in list:
    number_of_items = list.index(item) + 1
    print(f"Item {number_of_items}: {item}")


list2 = [ "Juan", "Ana", "Pedro", "María", "Carlos", "Luisa", "Luis"]

for name in list2:
    if name.startswith("L"):
        print(f"Hola {name}, tu nombre empieza con la letra L")
    else:
        print(f"Hola {name}, tu nombre no empieza con la letra L")


list3 = [1, 2, 3, 4, 5]

value = 0

for number in list3:
    value += number
    print(f"El valor actual es: {value}")

word = "Python"
for letter in word:
    print(letter)

for letter in "hello":
    print(letter)

for number in [(1,2), (3,4), (5,6)]:
    print(number)

for a,b in [(1,2), (3,4), (5,6)]:
    print(a)
    print(b)

dictionary = {"a":1, "b":2, "c":3}

for key in dictionary:
    print(key)
    #print(dictionary[key])

for key in dictionary.items():
    print(key)

for key in dictionary.values():
    print(key)

for a,b in dictionary.items():
    print(a,b)

#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares por separado en las variables suma_pares y suma_impares respectivamente: lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]. Recuerda que el módulo (o resto) de un número dividido entre 2 es cero cuando el número es par y uno cuando es impar, es decir: num % 2 == 0 para valores pares y num % 2 == 1 para valores impares.

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for number in lista_numeros:
    if number % 2 == 0:
        suma_pares = suma_pares + number
        #suma_pares = suma_pares + 1
        #print(suma_pares)
    elif number % 2 == 1:
        suma_impares = suma_impares + number
        #print(suma_impares)
        # TODO: write code...

print(suma_pares)
print(suma_impares)
