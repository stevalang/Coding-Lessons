# n = int(input())
# l_positive = []
# l_negative = []
# for _ in range(n):
#     number = int(input())
#     if number >= 0:
#         l_positive.append(number)
#     else:
#         l_negative.append(number)
# print(l_positive)
# print(l_negative)
# print(f'Count of positives: {len(l_positive)}. Sum of negatives: {sum(l_negative)}')


n = int(input())
numbers = [int(input()) for _ in range(n)]
positives = [n for n in numbers if n >= 0]
negatives = [n for n in numbers if n < 0]
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')