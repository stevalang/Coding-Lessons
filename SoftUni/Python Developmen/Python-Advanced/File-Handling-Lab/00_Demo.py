l = [1, 2, 3]
 
try:
    print(l[2])
except IndexError:
    print('No such index')
finally:
    print('the final stuff')