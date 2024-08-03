'''
Armstrong number is a number that can be come again, if we divide the number into the digits and power them off
with that of the number of digits.
'''

#mechanism #1

'''num1 = int(input('Enter a number'))
num_of_digits = len(str(num1))
new_number = 0
for i in str(num1):
    new_number = new_number + pow(int(i),num_of_digits)

if new_number == num1:
    print('{} is an armstrong number'.format(num1))
else:
    print('{} is not an armstrong number'.format(num1))
'''
# Mechanism # 2 :

num1 = int(input('Enter a number'))
num_of_digits = len(str(num1))
is_armstrong = sum(list(map(lambda i : pow(int(i),num_of_digits), str(num1)))) == num1
if is_armstrong :
    print('{} is an armstrong number'.format(num1))
else:
    print('{} is not an armstrong number'.format(num1))

