def lesser_of_two_evens(a, b):
    result = 0
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    print(result)


def lesser_of_two_evens_min_max(a, b):
    result = 0
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


lesser_of_two_evens(int(input()), int(input()))
