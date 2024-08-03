
def array_diff(a, b):

    for i in b:
        loop_true = True
        while loop_true:
            if i in a:
                a.remove(i)
            else:
                loop_true = False
    return a

print(array_diff([1,2,3], [1,2]))