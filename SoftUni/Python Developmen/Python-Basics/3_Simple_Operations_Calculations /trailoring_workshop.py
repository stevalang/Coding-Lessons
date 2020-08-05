count_table = int(input())
length_in_meters = float(input())
width_in_meters = float(input())

price_cover = 7
price_square = 9

area_tables = count_table * (length_in_meters + 2 * 0.30) * (width_in_meters + 2 * 0.30)

area_quads = count_table * (length_in_meters / 2) * (length_in_meters / 2)

price_in_usd = area_tables * 7 + area_quads * 9

total_squar_price = count_table


price_in_bgn =  price_in_usd * 1.85

print(f'{price_in_usd:.2f} USD')
print(f'{price_in_bgn:.2f} BGN')