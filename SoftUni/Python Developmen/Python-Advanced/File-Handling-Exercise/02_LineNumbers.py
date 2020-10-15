import string
import os
try:
    lines = []
    with open('text.txt', 'r') as file:
        lines = file.readlines()

    with open('output.txt', 'x') as file:
        for idx, line in enumerate(lines):

            line_number = f'Line {idx + 1}:'
            letter_count = len(list(filter(lambda x: x in string.ascii_letters, line)))
            punc_count = len(list(filter(lambda x: x in string.punctuation, line)))
            file.write(f'{line_number} {line.strip()} ({letter_count})({punc_count})\n')
except FileExistsError:
    print('File exist')
    os.remove('output.txt')

