the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):
    print(f"{the_board['top-L']} | {the_board['top-M']} | {the_board['top-R']}")
    print(f"- + - + -")
    print(f"{the_board['mid-L']} | {the_board['mid-M']} | {the_board['mid-R']}")
    print(f"- + - + -")
    print(f"{the_board['low-L']} | {the_board['low-M']} | {the_board['low-R']}")


turn = "X"
for i in range(9):
    print_board(the_board)
    print(f'Turn for {turn} . Move on which space ')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)
