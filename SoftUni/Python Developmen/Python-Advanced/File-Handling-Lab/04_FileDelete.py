import os

try:
    os.remove('my_first_file.txt')
    print('File Successfully Deleted')
except FileNotFoundError:
    print('File already deleted!')
finally:
    pass
