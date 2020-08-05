'''
Simple Operations and Calculations - Exercise
Check: https://judge.softuni.bg/Contests/Compete/Index/1160#0
04. Tailoring Workshop
Condition:
A sewing workshop accepts orders for sewing tablecloths and tablecloths for restaurants. The tablecloths are rectangular,
the carriages are square, their number is always the same. The tablecloth should hang 30 cm from each edge of the table.
The side of the carriage is half the length of the tables.
Each order includes information about the number and size of tables.
Write a program that calculates the price of an order in dollars and levs,
as a square meter fabric for a rectangular tablecloth costs 7 dollars, and for a square - 9 dollars. The dollar exchange rate is BGN 1.85.
Entrance
The user enters 3 numbers, one per line:
Number of rectangular tables - integer;
Length of rectangular tables in meters - real number;
Width of rectangular tables in meters - a real number.
Exit
To print two numbers on the console: the price of the products in dollars and in levs:
o "{price in dollars} USD"
o "{price in BGN} BGN"
Format the results up to two decimal places.
'''


count_table = int(input())
length_in_meters = float(input())
width_in_meters = float(input())

price_cover = 7
price_square = 9

area_tables = count_table * (length_in_meters + 2 * 0.30) * (width_in_meters + 2 * 0.30)

area_quads = count_table * (length_in_meters / 2) * (length_in_meters / 2)

price_in_usd = area_tables * 7 + area_quads * 9

total_squar_price = count_table


price_in_bgn =  price_in_usd * 1.85

print(f'{price_in_usd:.2f} USD')
print(f'{price_in_bgn:.2f} BGN')
