n = int(input())

guest_list = set()
guests_showed_up = set()

for _ in range(n):
    guest = input()
    guest_list.add(guest)

while True:
    line = input()
    if line == 'END':
        break
    else:
        guest = line
        guests_showed_up.add(guest)

print(len(guest_list) - len(guests_showed_up))
print("\n".join(sorted(guest_list - guests_showed_up)))
