phonebook = {}

while True:
    command = input()
    if command.isdigit():
        n = command
        for _ in range(int(n)):
            name = input()
            if name in phonebook:
                print(f'{name} -> {phonebook[name]}')
            else:
                print(f'Contact {name} does not exist.')
        break
    else:
        name, phone_num = command.split('-')
        phonebook[name] = phone_num
