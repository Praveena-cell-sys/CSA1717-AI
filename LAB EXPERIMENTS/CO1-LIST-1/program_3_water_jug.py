# Water Jug problem using BFS (4L jug, 3L jug, target 2L)
from collections import deque

cap_x, cap_y, target = 4, 3, 2
queue = deque([((0, 0), [(0, 0)])])
visited = {(0, 0)}

while queue:
    (x, y), path = queue.popleft()

    if x == target or y == target:
        break

    moves = [
        (cap_x, y), (x, cap_y),
        (0, y), (x, 0),
        (x - min(x, cap_y - y), y + min(x, cap_y - y)),
        (x + min(y, cap_x - x), y - min(y, cap_x - x))
    ]

    for m in moves:
        if m not in visited:
            visited.add(m)
            queue.append((m, path + [m]))

print("(4L jug, 3L jug)")
for state in path:
    print(state)
print("Target reached in", len(path) - 1, "steps")
