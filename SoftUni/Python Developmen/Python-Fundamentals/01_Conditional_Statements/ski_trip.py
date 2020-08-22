days = float(input())
type_accommodation = input()
review = input()

nights = days - 1
discount = 0

room_for_one_person = 18
apartment = 25
president_apartment = 35
total_discount = 0
total_price = 0
if days < 10:
    if type_accommodation == 'room for one person':
        discount = 1
        total_discount = nights * room_for_one_person * discount
        total_price = nights * room_for_one_person
    elif type_accommodation == 'apartment':
        discount = 0.3
        total_discount = nights * apartment * discount
        total_price = nights * apartment - total_discount
    elif type_accommodation == 'president apartment':
        discount = 0.1
        total_discount = nights * president_apartment * discount
        total_price = nights * president_apartment - total_discount
elif 10 < days < 15:
    if type_accommodation == 'room for one person':
        discount = 1
        total_discount = nights * room_for_one_person * discount
        total_price = nights * room_for_one_person
    elif type_accommodation == 'apartment':
        discount = 0.35
        total_discount = nights * apartment * discount
        total_price = nights * apartment - total_discount
    elif type_accommodation == 'president apartment':
        discount = 0.15
        total_discount = nights * president_apartment * discount
        total_price = nights * president_apartment - total_discount
if days > 15:
    if type_accommodation == 'room for one person':
        discount = 1
        total_discount = nights * room_for_one_person * discount
        total_price = nights * room_for_one_person
    elif type_accommodation == 'apartment':
        discount = 0.5
        total_discount = nights * apartment * discount
        total_price = nights * apartment - total_discount
    elif type_accommodation == 'president apartment':
        discount = 0.2
        total_discount = nights * president_apartment * discount
        total_price = nights * president_apartment - total_discount

if review == 'positive':
    additional_tip = total_price * 0.25
    final_price = total_price + additional_tip

elif review == 'negative':
    additional_discount = total_price * 0.10
    final_price = total_price - additional_discount

print(f'{final_price:.2f}')
