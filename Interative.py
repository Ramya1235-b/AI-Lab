def depth_limited_search(graph, node, goal, depth):
    print(node, end=" ")

    if node == goal:
        return True

    if depth == 0:
        return False

    for neighbour in graph[node]:
        if depth_limited_search(graph, neighbour, goal, depth - 1):
            return True

    return False


def iddfs(graph, start, goal, max_depth):

    for depth in range(max_depth + 1):

        print("\nDepth", depth, ":", end=" ")

        if depth_limited_search(graph, start, goal, depth):
            print("\nGoal found at depth", depth)
            return

    print("\nGoal not found")


# Number of vertices
n = int(input("Enter number of vertices: "))

graph = {}

# Enter vertices and neighbours
for i in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input("Enter neighbours: ").split()
    graph[vertex] = neighbours


# Starting vertex
start = input("Enter starting vertex: ")

# Goal vertex
goal = input("Enter goal vertex: ")

# Maximum depth
max_depth = int(input("Enter maximum depth: "))


print("\nIDDFS Traversal:")
iddfs(graph, start, goal, max_depth)
