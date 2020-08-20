def all_digits(line):
    return get_all_characters_matching_condition(text, lambda char: char.isdigit())


def all_letters(line):
    return get_all_characters_matching_condition(text, lambda char: char.isalpha())


def all_other_characters(line):
    return get_all_characters_matching_condition(text, lambda char: not char.isalpha() and not char.isdigit())


def get_all_characters_matching_condition(line, condition_fn):
    result = ""
    for char in text:
        if condition_fn(char):
            result += char
    return result


text = input()

print(all_digits(text))
print(all_letters(text))
print(all_other_characters(text))
