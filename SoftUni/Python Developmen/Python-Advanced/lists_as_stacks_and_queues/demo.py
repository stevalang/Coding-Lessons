from collections import  deque
# #    0, 1, 2 linear data structure
# l = [1, 2, 3, ]
#
# print(l)
# l.append(5)
# print(l)
#
#
# l.insert(1, -777)
# print(l)
#
# l.pop()
# print(l)
#
# # dynamic size
# # grow
# # shrink
# # random element access
# # first
# # middle
# # last
#
#

bullets = deque(map(int, input().split(' ')))
print(bullets)
print(deque(reversed(bullets)))