def summer_69(*arr):
    nums = arr.split()
    for num in nums:
        if num == 6:
            while num != 9:
                nums.remove(num)


def summer_69_edu(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    print(total)
    return total


summer_69_edu([4, 5, 6, 7, 8, 9])