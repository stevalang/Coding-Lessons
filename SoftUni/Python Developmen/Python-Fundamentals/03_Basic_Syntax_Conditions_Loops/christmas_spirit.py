'''
It's time to get in a Christmas mood. You have to decorate the house in time for the big event, but you have limited days to do so.
You will receive allowed quantity for one type of decoration and days left until Christmas day to decorate the house.
There are 4 types of decorations and each piece costs a price
Ornament Set – 2$ a piece
Tree Skirt – 5$ a piece
Tree Garlands – 3$ a piece
Tree Lights – 15$ a piece
Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17. If you have bought Tree Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.
Every tenth day you lose 20 spirit, because your cat ruins all tree decorations and you have to rebuild the tree and buy one piece of tree skirt, garlands and lights. That is why you are forced to increase the allowed quantity with 2 at the beginning of every eleventh day.
Also if the last day is a tenth day the cat decides to demolish even more and ruins the Christmas turkey and you lose additional 30 spirit.
At the end you must print the total cost and the gained spirit.
'''


quantity = int(input())
days = int(input())

price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_lights = 15

total_spirit = 0
total_cost = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_spirit += 5
        total_cost += quantity * price_ornament_set
    if i % 3 == 0:
        if quantity % 2 == 0:
            total_cost += quantity * price_tree_skirt + quantity * price_tree_garlands
            total_spirit += 43
        else:
            total_cost += quantity * price_tree_skirt + quantity * price_tree_garlands
        total_spirit += 13
    if i % 5 == 0:
        total_cost += quantity * price_tree_lights
        total_spirit += 17
    if i % 10 == 0:
        total_cost += quantity * price_tree_lights + quantity * price_tree_garlands + quantity * price_tree_skirt
        total_spirit -= 20

    if i % 10 == 0:
        total_spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
