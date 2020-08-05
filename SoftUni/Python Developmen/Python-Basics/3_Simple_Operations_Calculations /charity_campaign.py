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