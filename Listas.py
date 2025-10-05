object1 = "Nails"
object2 = "Brush"
object3 = "Hammer"
object4 = "Pickaxe"

objets = ["Nails", "Brush", "Hammer", "Pickaxe"]

objets.append("Saw")
objets.insert(1, "Wrench")

for i , object in enumerate(objets):
    print(f"El objeto {i} es: {object}")