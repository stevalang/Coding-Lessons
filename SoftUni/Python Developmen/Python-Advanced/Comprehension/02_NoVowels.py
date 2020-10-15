vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = {c for c in vowels.copy()} | {c.upper() for c in vowels.copy()}
print(''.join([c for c in input()if c not in vowels]))
