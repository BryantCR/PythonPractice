list2 = ["apple", "banana", "cherry"]
list3 = ["date", "fig", "grape"]
list4 = list2 + list3

result = len(list2)
print(result)

result = list2[0]
print(result)

result = list2[0:2]
print(result)

result = list2 + list3
print(result)

print(list4)

list4.append("kiwi")
print(list4)

list4.pop(1) 
print(list4)
poped = list4.pop(1)
print(poped)

notorder = ["g", "e", "a", "c", "b", "d", "f"]
notorder.sort()
print("notorder sort: ", notorder)

notorder.reverse()
print("notorder reverse: ", notorder)

#list4.remove("fig")
#print(list4)

#list4.insert(1, "orange")
#print(list4)




