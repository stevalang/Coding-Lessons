all_guests = {
              'Alice': {'apple': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}
              }


def total_brought(guest, item):
    num_brought = 0
    for k, v in guest.item():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


print('Number of things being brought:')
print('- Apples  ' + str(total_brought(all_guests, 'apples')))
print('- Cups  ' + str(total_brought(all_guests, 'cups')))
print('- Cakes  ' + str(total_brought(all_guests, 'cakes')))
print('- Ham Sandwiches  ' + str(total_brought(all_guests, 'ham sandwiches')))
print('- Apple Pie  ' + str(total_brought(all_guests, 'apple pies')))


