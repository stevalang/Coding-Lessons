initial_points = int(input())
counter = 0
while initial_points > 0:
    counter += 1
    sector = input()
    if sector == "double ring":
        points = int(input())
        points *= 2
        initial_points -= points
    elif sector == "triple ring":
        points = int(input())
        points *= 3
        initial_points -= points
    elif sector == 'number section':
        points = int(input())
        initial_points -= points
    elif sector == 'bullseye':
        print(f"Congratulations! You won the game with a bullseye in {counter} moves!")
        break
    if initial_points == 0:
        print(f'Congratulations! You won the game in {counter} moves!')
    elif initial_points < 0:
        print(f"Sorry, you lost. Score difference: {abs(initial_points)}.")


