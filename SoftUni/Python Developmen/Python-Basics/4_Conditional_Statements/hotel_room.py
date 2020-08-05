month = input()
nights_count = int(input())


price_apartment = 0
price_studio = 0
discount_price_apartment = 0
discount_price_studio = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if nights_count >= 14:
        discount_price_studio = 0.3
        discount_price_apartment = 0.1
    elif nights_count > 7:
        discount_price_studio = 0.05

elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if nights_count > 14:
        discount_price_studio = 0.2
        discount_price_apartment = 0.1

elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77
    if nights_count > 14:
        discount_price_apartment = 0.1

total_discount_apartment = price_apartment * nights_count * discount_price_apartment
total_price_apartment = price_apartment * nights_count - total_discount_apartment
total_discount_studio = price_studio * nights_count * discount_price_studio
total_price_studio = price_studio * nights_count - total_discount_studio

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')

