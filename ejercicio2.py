nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

resultado = []

for i in nums:
    for j in nums:
        # Check if sum matches the target
        # And avoid duplicates: (i, j) and (j, i)
        if i + j == target and (i, j) not in resultado and (j, i) not in resultado:
            resultado.append((i, j))

print(resultado)