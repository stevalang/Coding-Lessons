movie_budget = float(input())
extras_count = int(input())
outfit_price = float(input())

scene = movie_budget * 0.1
outfit_total = extras_count * outfit_price
discount = outfit_total * 0.1

if extras_count > 150:
    outfit_total = outfit_total - discount

difference = abs(movie_budget - outfit_total - scene)

if scene + outfit_total > movie_budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')
