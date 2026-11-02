# Missionaries and Cannibals problem using BFS
# State = (missionaries on left, cannibals on left, boat side)
# boat: 1 = left, 0 = right
from collections import deque

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m != 0 and m < c:
        return False
    if (3 - m) != 0 and (3 - m) < (3 - c):
        return False
    return True

start, goal = (3, 3, 1), (0, 0, 0)
boat = [(1, 0), (2, 0), (0, 2), (0, 1), (1, 1)]

queue = deque([(start, [start])])
visited = {start}

while queue:
    (m, c, b), path = queue.popleft()
    if (m, c, b) == goal:
        break

    for dm, dc in boat:
        if b == 1:
            new = (m - dm, c - dc, 0)
        else:
            new = (m + dm, c + dc, 1)

        if valid(new[0], new[1]) and new not in visited:
            visited.add(new)
            queue.append((new, path + [new]))

for i, state in enumerate(path):
    print("Step", i, ":", state)
print("Solved in", len(path) - 1, "crossings")
