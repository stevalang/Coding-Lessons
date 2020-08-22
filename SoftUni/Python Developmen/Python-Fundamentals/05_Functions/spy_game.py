def spy_game(nums):
    count = 0
    count_zeros = 0
    for num in nums:
        count += 1
        while num == 0:
            count_zeros += 1
            break
        if count_zeros == 2 and 7 in nums[count-1::]:
            print(True)
            return True
    print(False)


spy_game([1,2,4,0,0,7,5])


def spy_game_edu(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
