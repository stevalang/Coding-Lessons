"""

Write a program that reads an input consisting of a name and adds it to a queue until "End" is received. If you
receive "Paid", print every customer name and empty the queue, otherwise we receive a client and we have to add him
to the queue. When we receive "End" we have to print the count of the remaining people in the queue in the format: "{
count} people remaining."

"""


from collections import deque


def solve_supermarket():
    names = deque()

    while True:
        command = input()
        if command == 'End':
            print(f'{len(names)} people remaining.')
            break
        if command == 'Paid':
            while names:
                print(names.popleft())
        else:
            names.append(command)


solve_supermarket()
