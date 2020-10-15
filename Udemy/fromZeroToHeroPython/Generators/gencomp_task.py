my_list = [1, 2, 3, 4, 5]

gen_comp = (item for item in my_list if item > 3)

for item in gen_comp:
    print(item)
