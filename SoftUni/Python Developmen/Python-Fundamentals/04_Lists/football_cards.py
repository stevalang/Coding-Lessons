"""
Most football fans love it for the goals and excitement. Well, this problem doesn't. You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11. Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee, and the team with less than 7 players loses.

A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g. the card 'B-7' means player #7 from team B received a card. (index 6 of the list)
The task: Given a list of cards (could be empty), return the number of remaining players on each team at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}". If the game was terminated print an additional line: "Game was terminated"
Note for the random tests: If a player that has already been sent off receives another card - ignore it.

"""

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
