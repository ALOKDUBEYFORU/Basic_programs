'''
Write a program to find the list of all the prime numbers in an interval
'''
'''
no_of_factors = 0
for i in range(2,10):
    for j in range(2,i):
        if i%j == 0:
            no_of_factors = no_of_factors + 1
    if no_of_factors == 0:
        print('{} is a prime number'.format(i))
    no_of_factors = 0

'''
# Using lambda
