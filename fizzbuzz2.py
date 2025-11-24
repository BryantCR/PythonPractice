def check (range1, range2):
    for i in range(range1, range2 + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

range1 = int(input("Ingrese el primer número del rango: "))
range2 = int(input("Ingrese el segundo número del rango: "))
print((f"Resultados de FizzBuzz desde {range1} hasta {range2}: {check (range1, range2)} "))