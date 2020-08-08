destination = input()
while destination != 'End':
    minimum_budget = float(input())
    savings = 0
    while savings < minimum_budget:
        savings += float(input())
    print(f'Going to {destination}!')
    destination = input()


