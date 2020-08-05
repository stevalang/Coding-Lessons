'''
Simple Operations and Calculations - Exercise
Check: https://judge.softuni.bg/Contests/Compete/Index/1160#0
06. Charity Campaign
Condition:
A charity fundraising campaign is being held at the confectionery, which may involve confectioners
from all over the country. Initially, we read from the console the number of days in which the campaign runs and the number of confectioners,
which will be included. Then in separate rows we get the amount of cakes, waffles and pancakes,
which will be prepared by a confectioner in one day. The following price list must be kept in mind:
Cake - BGN 45
Waffles - BGN 5.80.
Pancake - BGN 3.20.
1/8 of the final amount will be used to cover the cost of the products during the campaign.
Write a program that calculates the amount collected at the end of the campaign.
Entrance
5 lines are read from the console:
1. The number of days in which the campaign runs - an integer;
2. The number of confectioners - an integer;
3. The number of cakes - an integer;
4. The number of waffles - an integer;
5. The number of pancakes - an integer.
Exit
Print a number on the console:
the money collected is formatted to the second decimal place
'''


days_count = int(input())
bakers_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
crepes_count = int(input())

cake_price = 45
waffle_price = 5.8
crepe_price = 3.2

sum_cakes = cakes_count * cake_price
sum_waffles = waffles_count * waffle_price
sum_crepes = crepes_count * crepe_price

expenses = 1/8
total_sum = days_count * bakers_count * (sum_cakes + sum_waffles + sum_crepes)
total_sum_after_expenses = total_sum * expenses
price = total_sum - total_sum_after_expenses
print(f'{price:.2f}')
