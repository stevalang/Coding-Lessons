wagons = int(input())

train = wagons * [0]

text = input()
while text != 'End':
    command = text
    token = command.split(' ')

    if len(token) < 3:
        cmd = token[0]
        people = int(token[1])
    else:
        cmd = token[0]
        wagon = int(token[1])
        people = int(token[2])
    if cmd == 'add':
        train[-1] = train[-1] + people

    elif cmd == 'insert':
        train[wagon] = train[wagon] + people
    elif cmd == 'leave':
        train[wagon] = train[wagon] - people
    text = input()

print(train)
