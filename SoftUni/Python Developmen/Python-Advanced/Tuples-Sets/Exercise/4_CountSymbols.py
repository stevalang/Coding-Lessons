text = tuple(input())
unique_characters = sorted(set(text))

for letter in unique_characters:
    print(f'{letter}: {text.count(letter)} time/s')
