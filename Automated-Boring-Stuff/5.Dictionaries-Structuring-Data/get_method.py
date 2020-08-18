picnic_items = {'apples': 5, 'cup': 2}
x = 'I am bringing ' + str(picnic_items.get('cup', 0)) + ' cups.'
print(x)
y = 'I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.'
print(y)