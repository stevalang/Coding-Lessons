age = int(input())
laundry_price = float(input())
toy_price = int(input())

toy_count = 0
gift_money = 0
money_per_even_year = 10
for i in range(1, age + 1):
    if i % 2 == 0:
        gift_money += money_per_even_year
    else:
        toy_count += 1

toy_income = toy_price * toy_count
saved_money = toy_income + gift_money
diff = abs(saved_money - laundry_price)

if saved_money >= laundry_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
