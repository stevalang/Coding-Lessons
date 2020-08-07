# n = int(input())
# salary = int(input())
#
# facebook_penalty = 150
# instagram_penalty = 100
# reddit_penalty = 50
#
# facebook_count = 0
# instagram_count = 0
# reddit_count = 0
#
# for i in range(n):
#     website = input()
#     if website == 'Facebook':
#         facebook_count += 1
#     if website == 'Instagram':
#         instagram_count += 1
#     if website == 'Reddit':
#         reddit_count += 1
#
# total_penalty = facebook_count * facebook_penalty + instagram_count * instagram_penalty + reddit_count * reddit_penalty
# diff = salary - total_penalty
# if diff <= 0:
#     print(f'You have lost your salary.')
# else:
#     print(diff)

n = int(input())
salary = int(input())

for i in range(n):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
    if salary <= 0:
        print(f'You have lost your salary.')
        break
if salary > 0:
    print(salary)
