import random, sys
print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0
actions = ['r', 'p', 's']
actions_name = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

while True:
    print(f'{wins} Wins, {losses} Losses, {ties}, Ties')
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        action = input()
        if action == 'q':
            print(f'{wins} Wins, {losses} Losses, {ties}, Ties')
            sys.exit()
        if action == 'r' or action == 'p' or action == 's':
            break
        print(f"Type one of {', '.join(actions)} or q.")
    print(f'{actions_name[action].upper()} versus...')
    second_action = random.choice(actions)
    print(actions_name[second_action].upper())
    if second_action == action:
        print('It is tie!')
        ties += 1

    elif action == "p" and second_action == 'r':
        print('You win!')
        wins += 1
    elif action == 's' and second_action == 'p':
        print('You win!')
        wins += 1
    elif action == 'r' and second_action == 's':
        print('You win!')
        wins += 1
    else:
        print('You loose!')
        losses += 1


