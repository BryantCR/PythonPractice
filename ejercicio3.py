# Eliminar duplicados y mantener el orden
# Dada una lista de números, elimina los elementos duplicados sin usar set()
# porque set() cambia el orden original.

lista = [1, 2, 3, 2, 4, 1, 5]

def eliminar_duplicado(lista):
    resultado = []

    for elemento in lista:
        # Agregar solo si no está ya en resultado
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado

print(eliminar_duplicado(lista))