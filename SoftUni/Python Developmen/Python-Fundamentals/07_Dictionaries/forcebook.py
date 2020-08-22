force_user = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    args = line.split()
    side = args[0]
    command = args[1]
    name = args[2]
    if command == '|':
        if side not in force_user:
            force_user[side] = []
        force_user[side].append(name)
    else:
        if side not in force_user:
            force_user[side] = [name]
        else:
            a = force_user.pop(force_user[side][name])
            force_user


sorted_users = dict(sorted(force_user.items(), key=lambda x: x[1]))
for key, value in sorted_users.items():
    print(f'Side: {key}, Members: {len(value)}')
    for name in value:
        print(f'! {name}')