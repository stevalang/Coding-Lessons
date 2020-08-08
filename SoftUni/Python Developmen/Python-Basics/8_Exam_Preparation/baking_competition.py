participants = int(input())

total_bakery = 0
cookies_sum = 0
cakes_sum = 0
waffles_sum = 0

for person in range(participants):
    name = input()
    command = input()
    cookies_count = 0
    cakes_count = 0
    waffles_count = 0
    while command != 'Stop baking!':
        count = int(input())
        total_bakery += count
        if command == 'cookies':
            cookies_count += count
            cookies_sum += 1.50 * count
        elif command == 'cakes':
            cakes_count += count
            cakes_sum += 7.80 * count
        elif command == 'waffles':
            waffles_count += count
            waffles_sum += 2.30 * count
        command = input()
    print(f'{name} baked {cookies_count} cookies, {cakes_count} cakes and {waffles_count} waffles.')

total_sum = cookies_sum + cakes_sum + waffles_sum
print(f'All bakery sold: {total_bakery}')
print(f'Total sum for charity: {total_sum:.2f} lv.')



# participants = int(input())
#
# total_desert = 0
# for i in range(participants):
#     name = input()
#     line = input()
#     cookies = 0
#     cakes = 0
#     waffles = 0
#     cookies_count = 0
#     cakes_count = 0
#     waffles_count = 0
#     while line != 'Stop baking!':
#         dessert_count = int(input())
#         total_desert += dessert_count
#         if line == 'cookies':
#             cookies += dessert_count
#             cookies_count = 1.50 * dessert_count
#         if line == 'cakes':
#             cakes += dessert_count
#             cakes_count = 7.80 * dessert_count
#         if line == 'waffles':
#             waffles += dessert_count
#             waffles_count = 2.30 * dessert_count
#         line = input()
#     print(f'{name} baked {cookies_count} cookies, {cakes_count} cakes and {waffles_count} waffles.')
#
# total_sum = cookies_count + cakes_count + waffles_count
# print(f'All bakery sold: {total_desert}\nTotal sum for charity: {total_sum:.2f} lv.')