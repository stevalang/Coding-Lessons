def reverse(string):
    return string[::-1]


def get_multiline_input(prompt):
    print(prompt)
    multiline_input = ''
    while True:
        s = input()
        if s != '':
            multiline_input += s + "\n"
        else:
            break
    return multiline_input


# words = []
# while True:
#     command = input()
#     if command == 'end':
#         break
#     words.append(command)
#
# for word in words:
#     print(f'{word} = {reverse(word)}')


text = get_multiline_input("Please enter myltiply lines:")
print(text)



