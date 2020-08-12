input_string = input()
word_length = len(input_string)
for i in range(word_length - 1, -1, -1):
    letter = input_string[i]
    print(letter, end="")