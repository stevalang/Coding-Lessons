from collections import defaultdict

text = input()
d = defaultdict(int)

for ch in text:
    if ch == ' ':
        continue
    d[ch] += 1
    # if ch not in d:
    #     d[ch] = 0

    # if ch in d:
    #     d[ch] +=1
    # else:
    #     d[ch] = 1

for key,value in d.items():
    print(f"{key} -> {value}")
