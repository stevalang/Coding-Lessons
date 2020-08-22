# loading_bar_list = ["."] * 10
# print(loading_bar_list)
# a = "".join(loading_bar_list)
# print(a)
#
#
#
#
# mylist = [1, 2, 3]
#
# mylist.append(4)
# print(mylist)
#
# mylist.pop()
# print(mylist)
#

# def myfunc(a, b):
#     return sum


def myfunc(*args):
    out = []
    for i in range(len(args)):
        if args[i] % 2 == 0:
            out.append(args[i].lower())
        else:
            out.append(args[i].upper())
        return ''.join(out)

myfunc('Hotel')