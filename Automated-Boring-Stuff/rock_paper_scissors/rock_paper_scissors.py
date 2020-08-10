import random
print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0
actions = ['r', 'p', 's']
actions_name = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    action = input()
    if action == 'q':
        print(f'{wins} Wins, {losses} Losses, {ties}, Ties')
        break
    print(f'{actions_name[action].upper()} versus...')
    second_action = random.choice(actions)
    print(actions_name[second_action].upper())
    if second_action == action:
        print('It is tie!')
        ties += 1
        print(f'{wins} Wins, {losses} Losses, {ties}, Ties')
    elif action == "P" and second_action == 'R':
        print('You win!')
        wins += 1
        print(f'{wins} Wins, {losses} Losses, {ties}, Ties')
    elif action == 'S' and second_action == 'P':
        print('You win!')
        wins += 1
        print(f'{wins} Wins, {losses} Losses, {ties}, Ties')
    elif action == 'R' and second_action == 'S':
        print('You win!')
        wins += 1
        print(f'{wins} Wins, {losses} Losses, {ties}, Ties')
    else:
        print('You loose!')
        losses += 1
        print(f'{wins} Wins, {losses} Losses, {ties}, Ties')

