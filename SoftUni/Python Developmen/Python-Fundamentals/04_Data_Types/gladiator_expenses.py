lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# is_helmet_broken = False
# is_sword_broken = False
# is_shield_broken = False
# is_armor_broken = False

expenses = 0

for fights_loses_count in range(1, lost_fights + 1):
    if fights_loses_count % 2 == 0:
        # is_helmet_broken = True
        expenses += helmet_price
    if fights_loses_count % 3 == 0:
        # is_sword_broken = True
        expenses += sword_price
    if fights_loses_count % 6 == 0:
        # is_shield_broken = True
        expenses += shield_price
    if fights_loses_count % 12 == 0:
        # is_armor_broken = True
        expenses += armor_price


print(f"Gladiator expenses: {expenses:.2f} aureus")