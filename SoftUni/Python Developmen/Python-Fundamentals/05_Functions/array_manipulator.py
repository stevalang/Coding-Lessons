"""
Trifon has finally become a junior developer and has received his first task. It's about manipulating an array of integers. He is not quite happy about it, since he hates manipulating arrays. They are going to pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job. You, on the other hand, love arrays (and money) so you decide to try your luck.
The array may be manipulated by one of the following commands
exchange {index} – splits the array after the given index, and exchanges the places of the two resulting sub-arrays. E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
If the index is outside the boundaries of the array, print "Invalid index"
max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
If there are two or more equal min/max elements, return the index of the rightmost one
If a min/max even/odd element cannot be found, print "No matches"
first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
If the count is greater than the array length, print "Invalid count"
If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty array "[]"
end – stop taking input and print the final state of the array
Input
The input data should be read from the console.
On the first line, the initial array is received as a line of integers, separated by a single space
On the next lines, until the command "end" is received, you will receive the array manipulation commands
The input data will always be valid and in the format described. There is no need to check it explicitly.
Output
The output should be printed on the console.
On a separate line, print the output of the corresponding command
On the last line, print the final array in square brackets with its elements separated by a comma and a space 
See the examples below to get a better understanding of your task
Constraints
The number of input lines will be in the range [2 … 50].
The array elements will be integers in the range [0 … 1000].
The number of elements will be in the range [1 .. 50]
The split index will be an integer in the range [-231 … 231 – 1]
first/last count will be an integer in the range [1 … 231 – 1]
There will not be redundant whitespace anywhere in the input
Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.
"""

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
