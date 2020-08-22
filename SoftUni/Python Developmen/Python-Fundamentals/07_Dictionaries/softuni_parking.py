def register(dictionary, u, p):
    if u in dictionary:
        print(f"ERROR: already registered with plate number {p}")
    else:
        dictionary[u] = p
        print(f'{u} registered {p} successfully')

def unregister(dictionary, u):
    if u not in dictionary:
        print(f"ERROR: user {u} not found")
    else:
        dictionary.pop(u)
        print(f"{u} unregistered successfully")

def print_plates(dictionary, template):
    for u,p in dictionary.items():
        print(template.format(u,p))

users = {}

for _ in range(int(input())):
    args = input().split()
    command = args[0]
    name = args[1]
    if command == "register":
        plate = args[2]
        register(users, name, plate)
    else:
        unregister(users, name)


print_plates(users,"{} => {}")