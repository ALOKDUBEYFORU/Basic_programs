a = [1,2,3,4,5,6]
len_a = len(a)
print(len_a)
new_array = []
new_array = a[int(len_a/2):]
new_array.extend(a[:int(len_a/2)])
print(new_array)