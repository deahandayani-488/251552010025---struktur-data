# graph
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)

        for tetangga in graph[node]:
            dfs(tetangga)


dfs(1)

print("DFS dari 1:", visited)