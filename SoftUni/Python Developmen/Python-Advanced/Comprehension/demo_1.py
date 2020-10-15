def addTwoDigits(n):
    str_n = str(n)
    tokens = [int(x) for x in str_n]

    return tokens[0] + tokens[1]


res = addTwoDigits(29)
print(res)
