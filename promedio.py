lista = []
lista.append((input("Ingresa la primera calificación: ")))
lista.append((input("Ingresa la segunda calificación: ")))
lista.append((input("Ingresa la tercera calificación: ")))

print("Las calificaciones son:", lista)
promedio = sum(int(x) for x in lista) / len(lista)

print("El promedio es:", promedio)

if promedio >= 60:
    print("Aprobado")
else:  
    print("Reprobado")


def pro(lista):
    return sum(lista) / len(lista)
