def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# Number of vertices
n = int(input("Enter number of vertices: "))

graph = {}

# Input vertices and neighbours
for i in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input("Enter neighbours: ").split()
    graph[vertex] = neighbours

# Starting vertex
start = input("Enter starting vertex: ")

# Visited set
visited = set()

print("\nDFS Traversal:")
dfs(graph, start, visited)
