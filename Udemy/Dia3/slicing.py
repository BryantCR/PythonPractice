text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
slice1 = text[2:10:2]
print(slice1)  # Output: 'CEGI'
slice1 = text[2:10]
print(slice1)  # Output: 'CDEFGHIJ'
slice1 = text[2]
print(slice1)  # Output: 'C'
slice1 = text[2:]
print(slice1)  # Output: 'CDEFGHIJKLMNOPQRSTUVWXYZ'
slice1 = text[::3]
print(slice1)  # Output: 'ADGJMPSVY'
slice1 = text[::-1]
print(slice1)  # Output: 'ZYXWVUTSRQPONMLKJIHGFEDCBA'


#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
#"Controlar la complejidad es la esencia de la programación"
#Pista: "Controlar" tiene un largo de 9 caracteres.
frase = "Controlar la complejidad es la esencia de la programación"
slice1 = frase[0:9]
print(slice1)

#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado."Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
slice1 = frase[8::3]
print(slice1)

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
slice1 = frase[::-1]
print(slice1)
