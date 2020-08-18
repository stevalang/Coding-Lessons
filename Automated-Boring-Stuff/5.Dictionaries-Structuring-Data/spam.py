spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

for k, v, in spam.items():
    print(f'Key: {k} Value: {str(v)}')
    