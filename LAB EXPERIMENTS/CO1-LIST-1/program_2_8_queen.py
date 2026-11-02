# 8-Queens problem using backtracking
N = 8
board = []

def safe(row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(row):
    if row == N:
        return True
    for col in range(N):
        if safe(row, col):
            board.append(col)
            if solve(row + 1):
                return True
            board.pop()
    return False

solve(0)
print("Queen positions (row, column):")
for r in range(N):
    print(r, board[r])

print()
for r in range(N):
    for c in range(N):
        print("Q" if board[r] == c else ".", end=" ")
    print()
