"""
You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
Legend:
0 - empty space
1 - first player move
2 - second player move
Find out who the winner is. If the first player wins print "First player won", otherwise if the second player wins print "Second player won", otherwise print "Draw!"
"""

import numpy as np
import random
from time import sleep


# Creates an empty board
def create_board():
    return (np.array([[0, 0, 0]
                      [0, 0, 0]
                      [0, 0, 0]]))


# Check for empty places on board
def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

# Select a random place for the player

