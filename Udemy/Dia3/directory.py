dic = {'c1': 'valor1', 'c2': 'valor2', 'c3': 'valor3'}

print(type(dic))
print(dic)

print(dic['c2'])

result = dic['c3']
print(result)

cliente = {'nombre': 'Juan', 'edad': 28, 'ciudad': 'Madrid'}
consulta = cliente['edad']
print(consulta)

diccionario = {'a': 1, 'b': [10, 20, 30], 'c': {'d': 100, 'e': 200}}
print(diccionario['b'][1])  # Output: 20

test = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(test['c2'][1].upper())  # Output: 'E'

test2 = {1: 'uno', 2: 'dos', 3: 'tres'}
print(test2)

test2[4] = 'cuatro'
print(test2)

test2[1] = 'Uno'
print(test2)

print(test2.keys())
print(test2.values())
print(test2.items())

#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

#nombre: Karen
#apellido: Jurgens
#edad: 36
#ocupacion: Editora
#pais: Colombia
#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic["pais"] = "Colombia"
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
print(mi_dic)



