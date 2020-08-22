cards = input().split(" ")

team_a = [1] * 11
team_b = [1] * 11


for card in cards:
    token = card.split('-')
    team = token[0]
    player = int(token[1])

    if team == "A":
        team_a[player -1] = 0
    else:
        team_b[player -1] = 0

count_a = 0
count_b = 0

for i in range(11):
    if len(team_a) > 0:
        count_a += team_a[i]
    if len(team_a) > 0:
        count_b += team_b[i]
print(f'Team A - {count_a}; Team B - {count_b}')
if count_a < 7 or count_b < 7:
    print(f'Game was terminated')
