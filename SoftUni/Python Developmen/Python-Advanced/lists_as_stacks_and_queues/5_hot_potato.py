from collections import deque


def solve(people, n):

    players = deque(people)
    while len(players) > 1:
        players.rotate(-n)
        print(f"Removed {players.pop()}")
    winner = players.pop()
    print(f'Last is {winner}')


solve(input().split(' '), int(input()))