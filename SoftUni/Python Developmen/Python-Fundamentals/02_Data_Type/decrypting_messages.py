key = int(input())
lines_number = int(input())
word = []
for i in range(lines_number):
    letter = input()
    actual_letter = chr(ord(letter) + key)
    word.append(actual_letter)
string = ''.join(word)
print(string)

