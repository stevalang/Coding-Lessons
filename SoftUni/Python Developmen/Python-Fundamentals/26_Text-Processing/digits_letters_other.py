def all_digits(text):
    digits = ''
    for char in text:
        if char.isdigit():
            digits += char
    return digits


def all_letters(text):
    letters = ''
    for letter in text:
        if letter.isalpha():
            letters += letter
    return letters


def all_other_characters(text):
    symbols = ''
    for symbol in text:
        if not symbol.isalpha() and not symbol.isdigit():
            symbols += symbol
    return symbols

text = input()

print(all_digits(text))
print(all_letters(text))
print(all_other_characters(text))
