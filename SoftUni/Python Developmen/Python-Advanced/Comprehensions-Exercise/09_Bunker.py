def count_items(bunker):
    return sum([item['quantity']
                for items_by_category
                in bunker.values()
                for item
                in items_by_category.values()
                ])


def avg_quality(bunker):
    return sum([item['quality']
                for items_by_category
                in bunker.values()
                for item
                in items_by_category.values()
                ]) / len(bunker.keys())


bunker = {category_name: {} for category_name in input().split(', ')}

n = int(input())

for _ in range(n):
    item_type, item_name, item_properties = input().split(' - ')
    item_property = {pair.split(':')[0]: int(pair.split(':')[1])
                     for pair
                     in item_properties.split(';')}

    bunker[item_type][item_name] = item_property


print(f'Count of items: {count_items(bunker)}')
print(f'Average quality: {avg_quality(bunker):.2f}')

for category, item in bunker.items():
    print(f"{category} -> {', '.join(item.keys())}")
