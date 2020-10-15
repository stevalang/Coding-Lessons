# from collections import deque
# line = input().split('|')
#
#
# res = deque()
#
# for i in range(len(line)):
#     res.appendleft((line[i].split()))
#
# for row in res:
#     print(' '.join(row), end=' ')
#

output_list = [element
               for row in reversed([outer_list.split()
                                    for outer_list in input().split('|')])
               for element in row]

print(' '.join(output_list))
