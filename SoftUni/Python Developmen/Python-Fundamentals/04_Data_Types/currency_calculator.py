fx_rates = {
    'USD': 1.31,
    'BGN': 2.35,
    'RUB': 42.1,
}

pounds_amount = float(input('Please enter amount in pounds:'))
target_currency = input('Please enter target currency:')

pound_fx_to_currency = fx_rates[target_currency]
amount_in_currency = pounds_amount * pound_fx_to_currency

print(f'{amount_in_currency:.2f} {target_currency}')