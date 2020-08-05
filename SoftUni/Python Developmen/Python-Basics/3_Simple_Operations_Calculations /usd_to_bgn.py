'''
Simple Operations and Calculations - Exercise
01. USD to BGN
Check: https://judge.softuni.bg/Contests/Compete/Index/1160#0
Write a program for converting US dollars (USD) into Bulgarian levs (BGN).
Round the result to 2 digits after the decimal point.
Use a fixed exchange rate between the dollar and the lev: 1 USD = 1.79549 BGN.
'''

usd = float(input())
bgn = usd * 1.79549
print(f'{bgn:.2f}')
