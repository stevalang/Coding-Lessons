from collections import deque


def solve_supermarket():
    queue = deque([])

    print()
    while True:
        command = input()
        if command == 'End':
            print(f"{len(queue)} people remaining.")
            break
        if command == 'Paid':
            while queue:
                print(queue.popleft())
        else:
            name = command
            queue.append(name)


solve_supermarket()
