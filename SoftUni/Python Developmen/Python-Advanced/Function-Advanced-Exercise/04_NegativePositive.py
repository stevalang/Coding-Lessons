nums = list(map(lambda number: int(number), input().split()))

sum_positive = sum(filter(lambda num: num > 0, nums))
sum_negative = sum(filter(lambda num: num < 0, nums))

print(sum_negative)
print(sum_positive)

if abs(sum_negative) > sum_positive:
    print(f'The negatives are stronger than the positives')
elif abs(sum_negative) < sum_positive:
    print(f"The positives are stronger than the negatives")