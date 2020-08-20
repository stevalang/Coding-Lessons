def master_yoga(text):
    words = text.split(' ')
    reverse = words[::-1]
    return ' '.join(reverse)


print(master_yoga('We are ready'))
