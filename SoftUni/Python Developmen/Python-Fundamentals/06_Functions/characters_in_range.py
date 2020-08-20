def string(a=input(), b=input()):
    new_string = []
    start = ord(a)
    finish = ord(b)
    for i in range(start+1, finish):
        new_string += [chr(i)]
    return ' '.join(new_string)


print(string())
