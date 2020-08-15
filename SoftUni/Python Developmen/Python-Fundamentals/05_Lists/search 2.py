lines = int(input())
special_word = input()
my_list = []
special_list = []
for _ in range(lines):
    word = input()
    if special_word in word:
        special_list.append(word)
    my_list.append(word)
print(my_list)
print(special_list)
