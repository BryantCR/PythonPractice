name = "Carina"
#name[0] = "K"  # Esto generará un error porque las cadenas son inmutables
name = "K" + name[1:]
print(name)

print(name * 10)

poem = """Roses are red,
Violets are blue, 
you are as beautiful as the sky so true."""
print(poem)
print("sky" in poem)
print("red" not in poem)
print(len(poem))

#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
text = "Repetición"
print(text*15)