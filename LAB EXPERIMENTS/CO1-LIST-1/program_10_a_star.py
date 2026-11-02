# A* algorithm: f(n) = g(n) + h(n)

graph = {
    "S": {"A": 1, "B": 4},
    "A": {"B": 2, "C": 5},
    "B": {"C": 2},
    "C": {"D": 3},
    "D": {}
}

h = {"S": 7, "A": 6, "B": 4, "C": 2, "D": 0}
open_list = [("S", 0, ["S"])]
closed = []

while open_list:
    open_list.sort(key=lambda item: item[1] + h[item[0]])
    node, g, path = open_list.pop(0)

    if node in closed:
        continue

    closed.append(node)
    print("Expand", node, ": g =", g, "h =", h[node], "f =", g + h[node])

    if node == "D":
        break

    for nxt in graph[node]:
        open_list.append((nxt, g + graph[node][nxt], path + [nxt]))

print()
print("Path:", " -> ".join(path))
print("Cost:", g)
