text = "this is a test string"  
result = text[0]

print(result)  # Output: 't'

result = text[-1]
print(result)  # Output: 'g'

result2 = text.index("a")
print(result2)  # Output: 8

result2 = text.index("test")
print(result2)  # Output: 10

result2 = text.index("s", 4)
print(result2)  # Output: 6

result2 = text.index("a", 4, 9)
print(result2)  # Output: 8

result2 = text.rindex("n")
print(result2)  # Output: 19

#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
result2 = frase.rindex("práctica")
print(result2)
