mytuple = (10, 20, 30, 40, 50)
print(type(mytuple))
print(mytuple)

print(mytuple[0])
print(mytuple[-1]) 
print(mytuple[1:4])

mytuple2 = ("Hola", 100, 3.14, True)
print(mytuple2)
print(mytuple2[0])
print(mytuple2[1:3])
print(mytuple2[-1])

mytuple3 = (10, (20, 30))
print(mytuple3)
print(mytuple3[1])
print(mytuple3[1][0])

mytuple4 = list(mytuple3)
print(type(mytuple4))

t = (1, 2, 3, 1)
a, b, c, d = t
print(a, b, c)
print(len(t))
print(t.count(1)) # Output: 2
print(t.index(3)) # Output: 2 