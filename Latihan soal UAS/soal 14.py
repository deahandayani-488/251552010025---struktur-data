from collections import deque

# adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for tetangga in graph[node]:
                queue.append(tetangga)

    return visited


print("BFS dari A:", bfs('A'))