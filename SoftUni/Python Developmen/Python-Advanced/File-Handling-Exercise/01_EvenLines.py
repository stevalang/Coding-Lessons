try:
    with open('text.txt') as text:
        symbols = ["-", ",", ".", "!", "?"]
        for idx, line in enumerate(text):
            for symbol in symbols:
                line = line.replace(symbol, '@')
                line_list = line.split()
                reverse_line_lst = reversed(line_list)
                output = ' '.join(reverse_line_lst)
            if idx % 2 == 0:
                print(output)

except FileNotFoundError:
    print('File not found')









