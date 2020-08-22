from collections import defaultdict

words_with_synonyms = defaultdict(list)

for _ in range(int(input())):
    word = input()
    synonym  = input()
    words_with_synonyms[word].append(synonym)

for word, synonym in words_with_synonyms.items():
    print(f"{word} - {', '.join(synonym)}")
