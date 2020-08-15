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

