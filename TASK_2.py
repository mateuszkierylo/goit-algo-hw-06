import networkx as nx

# Create the graph representing the transportation network
G = nx.Graph()

# Adding nodes (stations)
stations = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
G.add_nodes_from(stations)

# Adding edges (routes)
routes = [
    ("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"),
    ("D", "E"), ("D", "F"), ("E", "G"), ("F", "G"), ("G", "H"),
    ("H", "I"), ("G", "I"), ("F", "I")
]
G.add_edges_from(routes)

# DFS implementation
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            new_path = dfs(graph, node, goal, path)
            if new_path:
                return new_path
    return None

# BFS implementation
def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
    return None

# Finding paths
start_node = "A"
goal_node = "I"

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)