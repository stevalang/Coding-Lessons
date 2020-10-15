from collections import deque
expression = deque(input().split())
print(expression)

temp_numbers = []
while len(expression) > 1:
    current_element = expression.popleft()
    if current_element.isdigit():
        temp_numbers.append(current_element)
    else:
        pass
# expr = {'-':
#         '*'}
#
# for i in string:
#     if i.isdigit():

