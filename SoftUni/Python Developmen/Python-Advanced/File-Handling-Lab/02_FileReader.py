
print(sum(list(map(lambda num: int(num.rstrip('\n')), open('numbers.txt').readlines()))))
