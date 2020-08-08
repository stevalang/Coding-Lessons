budget = int(input())
towel_price = float(input())
discount = int(input())
umbrella = towel_price * 2 / 3
flip_flops = umbrella * 0.75
bag = (towel_price + flip_flops) / 3
total_purchase = towel_price + umbrella + flip_flops + bag
discount_sum = total_purchase * discount/100
price_after_discount = total_purchase - discount_sum
diff = abs(budget - price_after_discount)
if budget >= price_after_discount:
    print(f"Annie's sum is {price_after_discount:.2f} lv. She has {diff:.2f} lv. left.")
else:
    print(f"Annie's sum is {price_after_discount:.2f} lv. She needs {diff:.2f} lv. more.")