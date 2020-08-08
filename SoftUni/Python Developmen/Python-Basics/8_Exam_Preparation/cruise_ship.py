cruise_type = input()
cabin_type = input()
nights = int(input())
price = 0
if cruise_type == "Mediterranean":
    if cabin_type == "standard cabin":
        price = 27.50
    elif cabin_type == "cabin with balcony":
        price = 30.20
    elif cabin_type == "apartment":
        price = 40.50
elif cruise_type == "Adriatic":
    if cabin_type == "standard cabin":
        price = 22.99
    elif cabin_type == "cabin with balcony":
        price = 25.00
    elif cabin_type == "apartment":
        price = 34.99
elif cruise_type == "Aegean":
    if cabin_type == "standard cabin":
        price = 23.00
    elif cabin_type == "cabin with balcony":
        price = 26.60
    elif cabin_type == "apartment":
        price = 39.80
if nights > 7:
    price *= 0.75
total_price = price * nights * 4
print(f"Annie's holiday in the {cruise_type} sea costs {total_price:.2f} lv.")
