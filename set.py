#SET

tienda = {"Manzana", "Huevos", "Arroz", "Frijoles", "Frijoles"}
bodega = {"Arroz", "Frijoles", "Sardinas", "Salmón"}

ambos = tienda & bodega

norepite = tienda - bodega
norepite.add("Naranja")
norepite.update(["Pera", "Melón"])
norepite.remove("Naranja")

#for i, producto in enumerate(ambos, start = 1):
    #print(f"{i} se repite: {producto}")

for i, producto in enumerate(norepite, start = 1):
    print(f"{i} se repite: {producto}")

#print(tienda)
#print(bodega)

#def sets():
    #print ("esto es tienda: " + str(tienda))