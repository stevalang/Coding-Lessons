def paper_doll(text):
    string = []
    for i in range(len(text)):
        new_text = text[i] * 3
        string.append(new_text)
    out = ''.join(string)
    print(out)
    return out


def paper_doll_concat(text):
    result = ''

    for char in text:
        result += char * 3
    return result


paper_doll(input())