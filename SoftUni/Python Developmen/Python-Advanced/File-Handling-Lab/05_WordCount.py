import re
print()
with open('words.txt') as words_fh, open('text.txt') as words_fh1:
    words = words_fh.read().split()
    text = words_fh1.read()


words_occurrences = {}

for word in words:
    matches = \
        re.findall(rf'[\s-]({word})[\s.,?!]', text, re.MULTILINE + re.IGNORECASE)
    words_occurrences[word.lower()] = len(matches)


with open('output.txt', 'w') as output_fh:
    for word, occurrence in sorted(words_occurrences.items(), key=lambda t: -t[1]):
        print(f'{word} - {occurrence}', file=output_fh)
