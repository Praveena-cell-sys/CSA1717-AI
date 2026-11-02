# 8-Puzzle problem using BFS (0 means the blank tile)
from collections import deque

start = "123506478"
goal = "123456780"

def get_moves(state):
    moves = []
    i = state.index("0")
    row, col = i // 3, i % 3
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            s = list(state)
            s[i], s[j] = s[j], s[i]
            moves.append("".join(s))
    return moves

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()
    if state == goal:
        break
    for nxt in get_moves(state):
        if nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, path + [nxt]))

for step, s in enumerate(path):
    print("Step", step)
    print(s[0], s[1], s[2])
    print(s[3], s[4], s[5])
    print(s[6], s[7], s[8])
    print()

print("Solved in", len(path) - 1, "moves")
