string_of_numbers = input().split(' ')
stack_reversed_numbers = []

while string_of_numbers:
    stack_reversed_numbers.append(string_of_numbers.pop())

print(' '.join(stack_reversed_numbers))
