# d = {'a': 4, 'b': 5}
#
# print(d)
#
# a = map(lambda item: (item[0] + 'baba', item[1]), d.items())
# print(a)
# a = dict(a)
# print(a)
from collections import defaultdict
occurrences = defaultdict(int)
words = [w.lower() for w in input().split()]
for word in words:
    occurrences[word] += 1
print(" ".join(list([item[0] for item in filter(lambda item: item[1] % 2 !=0, occurrences.items())])))
