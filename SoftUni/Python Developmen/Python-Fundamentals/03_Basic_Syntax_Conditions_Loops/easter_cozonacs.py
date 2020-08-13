'''
Since it’s Easter you have decided to make some cozonacs and exchange them for eggs.
Create a program that calculates how much cozonacs you can make with the budget you have. First, you will receive your budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one cozonac:
'''

budget = float(input())
flour_kg_price = float(input())

eggs = flour_kg_price * 0.75
milk_litter = 1.25 * flour_kg_price
milk_for_one_cozonacs = milk_litter / 4
price_cozonac = eggs + flour_kg_price + milk_for_one_cozonacs

cozonac_counter =0
eggs_counter = 0
times_three_eggs = 0
while True:
    budget_cozonac = budget / price_cozonac
    if int(budget_cozonac) > cozonac_counter:
        eggs_counter += 3
        cozonac_counter += 1
        if cozonac_counter % 3 == 0:
            eggs_counter -= (cozonac_counter - 2)
    else:
        break
print(f"You made {cozonac_counter} cozonacs! Now you have {eggs_counter} eggs and {budget - price_cozonac * cozonac_counter:.2f}BGN left.")
