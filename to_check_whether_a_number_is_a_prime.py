'''
To check whether a number is prime
'''

'''
number = int(input('enter a number'))
no_of_factors = 0
for i in range(2,number+1):
    if number%i == 0 :
        no_of_factors = no_of_factors + 1
if no_of_factors == 1 :
    print(f'{number} is a prime number ')
else:
    print(f'{number} is not a prime number')

'''
number = int(input('enter a number'))
no_of_factors = 0
y = sum(list(map(lambda x: x%i,range(2,number+1))))
print(y(number))
