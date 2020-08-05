price_whiskey = float(input())
volume_beer_litters = float(input())
volume_wine_litters = float(input())
volume_rakia_litters = float(input())
volume_whiskey_litters = float(input())

price_rakia = price_whiskey / 2
price_wine = price_rakia * 0.6
price_beer = price_rakia * 0.2

money_rakia = volume_rakia_litters * price_rakia
money_beer = price_beer * volume_beer_litters
money_wine = price_wine * volume_wine_litters
money_whiskey = price_whiskey * volume_whiskey_litters

money_needed = money_beer + money_whiskey + money_wine + money_rakia

print(f'{money_needed:.2f}')