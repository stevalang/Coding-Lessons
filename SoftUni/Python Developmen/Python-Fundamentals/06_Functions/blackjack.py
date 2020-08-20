def blackjack(a=int, b=int, c=int):
    sum_num = sum([a, b, c])
    new_sum = sum_num - 10
    if sum([a, b, c]) <= 21:
        print(sum_num)
        return sum_num
    elif 11 in [a, b, c] and sum([a, b, c])-10 <= 21:
        print(sum([a, b, c])-10)
        return sum([a, b, c]) - 10
    else:
        print("BUST")


blackjack(9,9,9)