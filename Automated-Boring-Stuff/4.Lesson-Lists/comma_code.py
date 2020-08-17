spam = []

def list_to_str(l):
    text = ''
    for item in l:
        if text == '':
            text += item
        else:
            text += ', ' + item
    return text


x = list_to_str(spam)
print(x)
