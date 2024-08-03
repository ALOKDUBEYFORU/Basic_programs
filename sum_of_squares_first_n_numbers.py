'''
Calculation of sum of first n natural numbers
'''

import datetime

input1  = int(input('enter the number upto which sum of squares needed'))
inp_time1 = datetime.datetime.now()
sum1 = 0
for i in range(1,input1+1):
    sum1 = sum1 + i*i

print(f'{sum1} is the sum of squares of {input1} natural numbers')
out_time1 = datetime.datetime.now()

inp_time2 = datetime.datetime.now()
sum1 = 0
x = sum(list(map(lambda y:y*y,range(1,input1+1))))
print(x)
out_time2 = datetime.datetime.now()

inp_time3 = datetime.datetime.now()
def rec_square(input1):
    if input1 == 1 :
        return 1
    else:
        return input1*input1+rec_square(input1-1)

print(rec_square(input1))
out_time3 = datetime.datetime.now()

print(f"{out_time1 - inp_time1},{out_time2 - inp_time2},{out_time3 - inp_time3}")
