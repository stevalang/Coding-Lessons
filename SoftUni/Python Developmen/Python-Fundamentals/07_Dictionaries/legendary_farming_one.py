def validate_key_existing(dictionary, key,def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


materials = {
    'fragments': 0,
    'shards': 0,
    "motes": 0
}

legendary_items = {
    'fragments': "Valanyr",
    'shards': "Shadowmourne",
    "motes": "Dragonwrath"
}

junks = {}

winner = ""

while winner == "":
    args = input().lower().split()
    for i in range(0, len(args), 2):
        quantity = int(args[i])
        material = args[i + 1]


        if material in materials:
            materials[material] += quantity

            if materials[material] >= 250:
                winner = material
                break
        else:
            validate_key_existing(junks, material)
            junks[material] += quantity

materials[winner] -= 250
print(f"{legendary_items[winner]} obtained!")

sorted_dict_materials = dict(sorted(materials.items(), key=lambda el:(-el[1], el[0])))

sorted_dict_junks = dict(sorted(junks.items(), key=lambda el:el[0]))

# for k,v in sorted_dict_materials.items():
#     print(f"{k}: {v}")
# for k,v in sorted_dict_junks.items():
#     print(f"{k}: {v}")

print_dict(materials, "{}: {}")
print_dict(junks, "{}: {}")