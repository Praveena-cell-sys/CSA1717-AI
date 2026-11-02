# Travelling Salesman Problem - try every route (brute force)
from itertools import permutations

# distance[i][j] = distance from city i to city j
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
names = "ABCD"

best_cost = 999
best_route = None

for route in permutations([1, 2, 3]):
    path = [0] + list(route) + [0]
    cost = 0

    for i in range(len(path) - 1):
        cost += distance[path[i]][path[i + 1]]

    print("".join(names[c] for c in path), "cost =", cost)

    if cost < best_cost:
        best_cost = cost
        best_route = path

print()
print("Best route:", "".join(names[c] for c in best_route))
print("Minimum cost:", best_cost)
