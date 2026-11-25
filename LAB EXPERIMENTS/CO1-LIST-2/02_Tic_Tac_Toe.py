# PROGRAM
board = [' '] * 9

def show():
    print()
    for i in range(0, 9, 3):
        print(' ' + ' | '.join(board[i:i+3]))
        if i < 6:
            print('---+---+---')
    print()

def winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

player = 'X'
for turn in range(9):
    show()
    move = int(input(f"Player {player}, enter position (1-9): ")) - 1
    while move < 0 or move > 8 or board[move] != ' ':
        move = int(input("Invalid move. Try again (1-9): ")) - 1
    board[move] = player
    if winner():
        show()
        print(f"Player {player} wins!")
        break
    player = 'O' if player == 'X' else 'X'
else:
    show()
    print("It's a draw!")

# SAMPLE OUTPUT
#   |   |
# ---+---+---
#   |   |
# ---+---+---
#   |   |
#
# Player X, enter position (1-9): 1
# X |   |
# ---+---+---
#   |   |
# ---+---+---
#   |   |
#
# Player O, enter position (1-9): 4
# X |   |
# ---+---+---
# O |   |
# ---+---+---
#   |   |
#
# Player X, enter position (1-9): 2
# X | X |
# ---+---+---
# O |   |
# ---+---+---
#   |   |
#
# Player O, enter position (1-9): 5
# X | X |
# ---+---+---
# O | O |
# ---+---+---
#   |   |
#
# Player X, enter position (1-9): 3
# X | X | X
# ---+---+---
# O | O |
# ---+---+---
#   |   |
#
# Player X wins!
