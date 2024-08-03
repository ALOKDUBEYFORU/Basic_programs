
'''
Printing nth term of a fibonacci series
'''

a = 0
number  = int(input('enter nth term of a fibonacci series'))
last_num = 0
for i in range(0,number):
    if i == 1 :
        a = 1
    print(a,last_num)
    last_num,a = a,a+last_num
print(last_num)