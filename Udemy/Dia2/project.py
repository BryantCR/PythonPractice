name = str(input("Dime tu nombre: "))
sales = int(input("Dime tus venas: "))
bonus = sales * 13 / 100
print(type(sales))
print(type(bonus))

print(f"Hola {name} tu bono es de {round(bonus, 2)}")