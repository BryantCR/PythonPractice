if 10 > 9:
    print("es verdadero")


if 10 < 9:
    print("es verdadero")
else:
    print("es falso")

pet = "d"

if pet == "dog":
    print("It's a dog")
elif pet == "cat":
    print("It's a cat")
elif pet == "fish":
    print("It's a fish")
else:
    print("It's not a dog")

age = 18
grades = 85

if age >= 18:
    print("You are an adult")
    if grades >= 70:
        print("You passed the course")
    elif grades < 70:
        print("You failed the course")
if age < 18:
    print("You are a minor")


num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")


edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")
