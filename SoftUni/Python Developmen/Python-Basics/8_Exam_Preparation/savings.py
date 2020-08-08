income = float(input())
months = int(input())
expenses = float(input())

emergency_fund = income * 0.3
money_left = income - (expenses + emergency_fund)
all_money_saved = months * money_left
percentage_save = money_left/ income * 100
print(f'She can save {percentage_save:.2f}% \n{all_money_saved:.2f}')
