# eggs = ('hello', 42, 0.5)
# print(eggs[0])
# print(eggs[1:3])
# print(len(eggs))
#
# print(tuple(['cat', 'dog', 5]))
# print(list(('cat', 'dog', 5)))
# print(list('hello'))
#
#
# spam = 42
# cheese = spam
# spam = 100
# print(spam)
# print(cheese)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # The reference is being copied, not the list
cheese[1] = 'Hello!'  # This changes the list value.
print(spam)