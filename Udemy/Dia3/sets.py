my_set = set([1,2,3,4,5,1,1,1,1,2,2,2,2,(10,20,30)])
print(type(my_set))
print(len(my_set))

my_set2 = {10, 20, 30, 40, 50}
print(type(my_set2))
print(my_set2)

print(my_set)
print(3 in my_set)
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)

my_set.discard(10)
print(my_set)

my_set.clear()
print(my_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.pop()
print(s1)