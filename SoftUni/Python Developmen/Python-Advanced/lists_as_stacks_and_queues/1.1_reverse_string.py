def solve(str):
    reversed_str = ''
    s = list(str)

    while s:
        reversed_str += s.pop()
    return reversed_str


print(solve('I love Python'))
print(solve('Stacks and Queues'))
