words: list = input().split(' ')
print(''.join(map(lambda word: word * len(word), words)))
