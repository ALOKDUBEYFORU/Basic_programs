'''
To find out the largest element of the list
'''
import random
array1 = []
for i in range(20):
    array1.append(random.randint(0,20))

print(f'{max(array1)} is the highest element of {array1}')

array1 = []
for i in range(20):
    array1.append(random.randint(0,30))

print('{} is the largest element of {}'.format(sorted(array1)[-1],array1))

