# Depth First Search (DFS)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print("Visited:", node)
        for neighbour in graph[node]:
            dfs(neighbour)

dfs("A")
print("DFS order:", visited)
