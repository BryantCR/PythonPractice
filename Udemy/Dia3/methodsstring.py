test = "Este es el texto de Bryan"

result = test
print(result)

result = test.upper()
print(result)

result = test[2].upper()
print(result)

result = test.lower()
print(result)

result = test.split()
print(result)

result = test.split("t")
print(result)

#result = test.join()
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)

result = test.find("Bryan")
print(result)

result = test.replace("Bryan", "Carlos")
print(result)   

#-----------------------------------MORE METHODS------------------------------------

result = test.capitalize()
print(result)  

result = test.title()
print(result)

result = test.count("e")
print(result)  

#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
e = " ".join(lista_palabras)
print("List to string", e)

#Reemplaza en la siguiente frase:"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:

#"difícil" --> "fácil"

#"mala" --> "buena"

#y muestra en pantalla la frase con ambas palabras modificadas.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
result = frase.replace("difícil", "fácil")
result2 = result.replace("mala", "buena")
print(result2)  