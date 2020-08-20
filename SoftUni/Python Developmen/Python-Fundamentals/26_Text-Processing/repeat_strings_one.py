def repeat_by_length(word):
    return word * len(word)


words: list = input().split(' ')
print(''.join(map(repeat_by_length, words)))