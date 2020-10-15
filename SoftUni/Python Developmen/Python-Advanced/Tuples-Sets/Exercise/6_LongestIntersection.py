n = int(input())

set_intersection_list = []

for _ in range(n):
    first, second = tuple(input().split('-'))
    first_start, first_end = tuple(map(int, str(first).split(',')))
    second_start, second_end = tuple(map(int, str(second).split(',')))
    set_one = set(range(first_start, first_end + 1))
    set_two = set(range(second_start, second_end + 1))
    set_intersection = set_one & set_two
    set_intersection_list.append(set_intersection)

longest_intersection = 0
index_longest = 0
index = 0

for intersection in set_intersection_list:
    set_size = len(intersection)
    if set_size > longest_intersection:
        longest_intersection = set_size
        index_longest = index
    index += 1

print(f"Longest intersection is {list(set_intersection_list[index_longest])} with length {longest_intersection}")
