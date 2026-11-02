# Breadth First Search (BFS)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = []
queue = ["A"]

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        print("Visited:", node)
        for neighbour in graph[node]:
            queue.append(neighbour)

print("BFS order:", visited)
