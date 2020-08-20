# import sys
# items = input().split()
# numbers = []
#
#
# def exchange(numbers, index):
#     temp_numbers = numbers[index + 1:]
#     temp_numbers += numbers[:index + 1]
#     return temp_numbers
#
#
# def get_index_max_even_num(numbers):
#     max_num = -sys.maxsize
#     index = -1
#
#     for i in range(len(numbers)):
#         num = numbers[i]
#         if num % 2 == 0 and num >= max_num:
#             max_num = num
#             index = i
#
#
# def get_index_max_odd_num(numbers):
#     max_num = -sys.maxsize
#     index = -1
#
#     for i in range(len(numbers)):
#         num = numbers[i]
#         if num % 2 != 0 and num >= max_num:
#             max_num = num
#             index = i
#
#
# for item in items:
#     numbers.append(int(item))
#
# command_input = input()
#
# while command_input != "end":
#     tokens = command_input.split()
#     command = tokens[0]
#
#     if command == 'exchange':
#         index = int(tokens[1])
#
#         if index < 0 or index >= len(numbers):
#             print("Invalid index")
#             command_input = input()
#             continue
#
#         numbers = exchange(numbers, index)
#
#     elif command == 'max':
#         criteria = tokens[1]
#
#         if criteria == ' even':
#             index = get_index_max_even_num(numbers)
#         elif criteria == 'odd':
#             index = get_index_max_odd_num(numbers)
#         if index != -1:
#             print(index)
#         else:
#             print("No matches")
#     elif command == 'min':
#         pass
#     elif command == 'first':
#         pass
#     elif command == 'last':
#         pass
#     command_input = input()

import sys
the_list = []


def exchange(command):
    global the_list
    index_to_exchange = int(command[1])
    if len(the_list) > index_to_exchange >= 0:
        the_list = the_list[index_to_exchange + 1:] + the_list[:index_to_exchange + 1]
    else:
        print("Invalid index")


def max_num(command):
    global the_list
    max_number = -sys.maxsize - 1
    index_of_number = -1
    if command[1] == "even":
        for number in range(len(the_list)):
            if the_list[number] % 2 == 0 and the_list[number] >= max_number:
                max_number = the_list[number]
                index_of_number = number
    elif command[1] == "odd":
        for number in range(len(the_list)):
            if the_list[number] % 2 != 0 and the_list[number] >= max_number:
                max_number = the_list[number]
                index_of_number = number
    if index_of_number == -1:
        print("no matches")
    else:
        print(index_of_number)


def min_num(command):
    global the_list
    min_number = sys.maxsize
    index_of_number = -1
    if command[1] == "even":
        for number in range(len(the_list)):
            if the_list[number] % 2 == 0 and the_list[number]<=min_number:
                min_number = the_list[number]
                index_of_number = number
    elif command[1] == "odd":
        for number in range(len(the_list)):
            if the_list[number] % 2 != 0 and the_list[number]<=min_number:
                min_number = the_list[number]
                index_of_number = number
    if index_of_number == -1:
        print("No matches")
    else:
        print(index_of_number)


def first(command):
    global the_list
    its_ok = True
    count_numbers = int(command[1])
    if count_numbers > len(the_list):
        print("Invalid count")
        its_ok = False
    if command[2] == "even" and its_ok:
        print([item for item in the_list if item % 2 == 0][:count_numbers])
    elif command[2] == "odd" and its_ok:
        print([item for item in the_list if item % 2 != 0][:count_numbers])


def last(command):
    global the_list
    its_ok = True
    count_numbers = int(command[1])
    if count_numbers > len(the_list):
        print("Invalid count")
        its_ok = False
    if command[2] == "even" and its_ok:
        print([item for item in the_list if item % 2 == 0][-count_numbers:])
    elif command[2] == "odd" and its_ok:
        print([item for item in the_list if item % 2 != 0][-count_numbers:])


def array_manipulator():
    global the_list
    the_list = [int(digit) for digit in input().split()]
    while True:
        command_ = input().split()
        if command_[0] == "end":
            break
        if command_[0] == "exchange":
            exchange(command_)
        elif command_[0] == "max":
            max_num(command_)
        elif command_[0] == "min":
            min_num(command_)
        elif command_[0] == "first":
            first(command_)
        elif command_[0] == "last":
            last(command_)
    print(the_list)


if __name__ == '__main__':
    array_manipulator()