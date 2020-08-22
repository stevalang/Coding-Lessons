sides = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

if "|" in line:
    args = line.split(" | ")
    side = args[0]
    user = args[1]

    if side not in sides:
        sides[side] = []

    if user not in sides[side]:
        sides[side].append(user)
    else:
        args = line.split(" -> ")
        user = args[0]
        side = args[1]
        old_side = ""

        for key, value in sides.items():
           if user in value:
            old_side = key
            break

        if old_side != "":
            sides[old_side].remove(user)
            sides[side].append(user)
        else:
            pass
