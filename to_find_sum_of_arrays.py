import random
array1 = []
for i in range(12):
    array1.append(random.randint(0,12))
print(array1)
print(f'{sum(array1)} is the sum of array')


array1 = []
sum1 = 0
for i in range(12):
    array1.append(random.randint(0,12))
    sum1 = sum1 + array1[i]
print(array1)
print(f'{sum1} is the sum of array')
