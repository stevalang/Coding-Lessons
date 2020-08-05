'''
Simple Operations and Calculations - Lab
08. Yard Greening
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1011#2
Божидара разполага с няколко къщи на Черноморието и желае да озелени дворовете на някои от тях, като по този начин
 създаде уютна обстановка и комфорт на гостите си, като за целта е наела фирма.
Напишете програма, която изчислява необходимите средства, които Божидара ще трябва да заплати на фирмата изпълнител
на проекта. Цената на един кв. м. е 7.61лв със ДДС. Тъй като нейният двор е доста голям, фирмата изпълнител предлага
18% отстъпка от крайната цена.
Вход
От конзолата се прочита само един ред:
1.	Кв. метри, които ще бъдат озеленени – реално число.
Изход
На конзолата се отпечатват два реда:
"The final price is: {крайна цена на услугата} lv."
"The discount is: {отстъпка} lv."
И двете суми трябва да бъдат форматирани до втората цифра след десетичния знак.
'''


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
