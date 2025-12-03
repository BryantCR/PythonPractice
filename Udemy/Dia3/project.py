user_text = str(input("""Ingrese un texto: """))
user_text = user_text.lower()
python_in_text = "python" in user_text
#word_count = len(user_text)
#print("La cantidad de caracteres en el texto es: ", word_count)
word_count = user_text.split()
rever_text = word_count[::-1]
e = " ".join(rever_text)


user_input = list(input("Ingrese 3 letras a su elección: "))

check_word1 = user_text.count(user_input[0]) 
check_word2 = user_text.count(user_input[1])
check_word3 = user_text.count(user_input[2])



print("El texto ingresado es: ", user_text)
print("Las letras ingresadas son: ", user_input)
print(f"La cantidad de veces que aparece la letra {user_input[0]} es: ", check_word1)
print(f"La cantidad de veces que aparece la letra {user_input[1]} es: ", check_word2)
print(f"La cantidad de veces que aparece la letra {user_input[2]} es: ", check_word3)
print("La cantidad de palabras en el texto es: ", len(word_count))
print("Las primera letra en el texto e: ", user_text[0])
print("Las última letra en el texto e: ", user_text[-1])
print("El texto invertido es: ", e)
print("¿La palabra 'python' está en el texto ingresado?: ", python_in_text)
