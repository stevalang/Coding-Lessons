# with open('my_first_file.txt', 'w') as f:
#     f.write('I just created my first file!')


f = open('my_first_file.txt', 'w')

try:
    f.write('I just created my first file!')
finally:
    f.close()
