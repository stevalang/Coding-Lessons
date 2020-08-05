budget = float(input())
seasons = input()
destination = ""
vacation_type = ""
cost = 0
if budget <= 100:
    destination = "Bulgaria"
    cost = budget * 0.3 if seasons == 'summer' else budget * 0.7
    vacation_type = "Camp" if seasons == 'summer' else "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    cost = budget * 0.4 if seasons == 'summer' else budget * 0.8
    vacation_type = "Camp" if seasons == 'summer' else "Hotel"
else:
    destination = "Europe"
    vacation_type = "Hotel"
    cost = budget * 0.9
print(f'Somewhere in {destination}\n{vacation_type} - {cost:.2f}')




# if budget <= 100:
#     destination = "Bulgaria"
#     if seasons == 'summer':
#         budget *= 0.3
#         vacation_type = 'Camp'
#     else:
#         budget *= 0.7
#         vacation_type = "Hotel"
# elif budget <= 1000:
#     destination = "Balkans"
#     if seasons == 'summer':
#         vacation_type = "Camp"
#         budget *= 0.4
#
#     else:
#         vacation_type = "Hotel"
#         budget *= 0.8
# else:
#     destination = "Europe"
#     vacation_type = "Hotel"
#     budget *= 0.9
#
# print(f'Somewhere in {destination}')
# print(f'{vacation_type} - {budget:.2f}')
