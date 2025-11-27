#Dada una lista de números enteros nums y un número target.
#Encuentra todos los pares (a, b)
#dentro de la lista tales que a+b=target.

nums = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target1= 10

def target(nums, target1):
    pares = []
    sumtarget = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            pares.append((nums[i]))
            for j in range(len(nums)):
                if nums[i] + nums[j] == target1 and (nums[i] + nums[j]) not in sumtarget and (nums[j] + nums[i]) not in sumtarget:
                    sumtarget.append((nums[i], nums[j]))
    return "Estos son los pares:", pares, "Estos son los que suman el target:", sumtarget

print(target(nums, target1))