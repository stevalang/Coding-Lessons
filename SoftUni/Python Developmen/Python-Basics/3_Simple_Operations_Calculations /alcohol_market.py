"""
Simple Operations and Calculations - Exercise
Check: https://judge.softuni.bg/Contests/Compete/Index/1160#0
07. Alcohol Market
Condition:
On foot he decides to have a party and goes to the alcohol exchange to buy beer, wine, brandy and whiskey. To write a program
which calculates how much money he needs to pay the bill, knowing that:
the price of brandy is half lower than that of whiskey;
the price of wine is 40% lower than the price of brandy;
the price of beer is 80% lower than the price of brandy.
Entrance
5 lines are read from the console:
1. Price of whiskey in BGN - real number;
2. Quantity of beer in liters - real number;
3. Quantity of wine in liters - real number;
4. Quantity of brandy in liters - real number;
5. Quantity of whiskey in liters - a real number.
Exit
Print a number on the console:
the money that Pesho needs, formatted to the second decimal place.
"""

price_whiskey = float(input())
volume_beer_litters = float(input())
volume_wine_litters = float(input())
volume_rakia_litters = float(input())
volume_whiskey_litters = float(input())

price_rakia = price_whiskey / 2
price_wine = price_rakia * 0.6
price_beer = price_rakia * 0.2

money_rakia = volume_rakia_litters * price_rakia
money_beer = price_beer * volume_beer_litters
money_wine = price_wine * volume_wine_litters
money_whiskey = price_whiskey * volume_whiskey_litters

money_needed = money_beer + money_whiskey + money_wine + money_rakia

print(f'{money_needed:.2f}')
