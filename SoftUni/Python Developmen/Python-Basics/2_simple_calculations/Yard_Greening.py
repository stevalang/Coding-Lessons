# 1. Read input data and covert data types
yard_area = float(input())

# 2. Calculate total cost money needed
cost_per_sq_meter = 7.61
total_money_needed = yard_area * cost_per_sq_meter

# 3. Calculate 18% discount
discount = (total_money_needed * 18) / 100

# 4. Calculate money needed without discount
total_money_needed_after_discount = total_money_needed-discount

# 5. Print and format
print(f'The final price is: {total_money_needed_after_discount:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')

# MY INITIAL SOLUTION
# price_m2 = 7.61
# discount = 0.18
# area = input()
# area = float(area)
# total_discount = area * price_m2 * discount
# total_price = area * price_m2 - total_discount
#
# print(f'The final price is {total_price:.2f} lv.')
# print(f"The discount is: {total_discount:.2f} lv.")
