# a = 1
# print(type(a))
# todo_list = ["Do the dishes", "Clean my room"]
# print(todo_list[-1])
# print(list())
# # help(list)
#
# some_text = " a b c d"
# print(some_text.split( ))

# l = []
# l.append(1)
# l.append(1)
# l.append(1)
# l.append(1)
# l.append(1)
# print(l)
# print(id(l))
#
import copy

#
# l = []
# m = copy.deepcopy(l)
# print(id(l))
# print(id(m))

# l = []
# m = l
# l.append(1)
# print(l)
# print(m)
#
# l = []
# m = copy.deepcopy(l)
# l.append(0)
# print(l)
# print(m)
# -----------------------------------------------------------
# a = ""
# help(str.join(a))
#
# l = ','.join(['baba', 'dqdo', 'test'])
# print(l)
# ---------------------------------------------------------------

# range(10)
# print(range(10))
#
# list(range(10))
# print(list(range(10)))

# range(10)[0]
# range(10)[1]
# range(10)[2]
# range(10)[3]
# print(range(10)[3])
# r = range(10)

# help(list.mro())

# l = [1, 2, 3]
# m = l[:]
#
# list_of_numbers = [1, 2, 3, 4]
# list_of_numbers.remove(1)
# print(list_of_numbers)

# my_list = ["dog", "cat", "fish"]
# for element in my_list:
#     print(element, end=" ") #dog cat fish
#
# for index in range(len(my_list)):
#     print(my_list[index], end=' ') # dog cat fish

# animals = ['dog', 'cat', 'giraffe']
# i = 0
# for animal in animals:
#     print(i, animal)
#     i += 1

# -------------------------

# enumerate(['dog', 'cat'])
# list(enumerate(['dog', 'cat'], 1))

# ---------------------------------
#
# animals = ['dog', 'cat', 'giraffe']
#
# for i, animal in enumerate(animals):
#     print(i, animal)
# -----------------------------------------
# help(zip)

# zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
# a = list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# print(a)

# ---------------------------

# my_list = ['baba', 'dqdo']
#
# while len(my_list) > 0:
#     element = my_list.pop(0)
#

# my_list = ['dog', 'cat', 'fish']
# while len(my_list) > 0:
#     print(my_list[0], end=" ")
#     my_list.pop(0)
#
# my_list = ["dog", "cat", "fish"]
# while len(my_list) > 0:
#     print(my_list.pop(0), end=" ")

# FILTER

# help(filter)
#
# def is_awesome(name):
#     return name == "python"
#
#
# is_awesome("java")
# is_awesome("c#")
# is_awesome("python")
#
# programming_languages = ['python', 'java', 'c#']
#
# filter(is_awesome, programming_languages)
# print(filter(is_awesome, programming_languages))
# list(filter(is_awesome, programming_languages))
# print(list(filter(is_awesome, programming_languages)))


# lambda
# is_awesome = lambda name: name in ['python']
# is_awesome("java")
# is_awesome("c#")
# is_awesome("python")
# programming_languages = ['python', 'java', 'c#']
#
#
#
# is_awesome('python')
#
# list(filter(lambda name: name == 'python', programming_languages))
# -------------------------------------------------

all()
