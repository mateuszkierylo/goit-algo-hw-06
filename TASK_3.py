import networkx as nx
import heapq

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

# Add weights to the edges (randomly chosen for this example)
weighted_edges = [
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 5), ("B", "D", 10), ("C", "E", 3),
    ("D", "E", 4), ("D", "F", 11), ("E", "G", 5), ("F", "G", 8), ("G", "H", 4),
    ("H", "I", 9), ("G", "I", 2), ("F", "I", 7)
]

# Create a weighted graph
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_edges)

# Dijkstra's algorithm
def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Find the shortest paths between all vertices
shortest_paths = {node: dijkstra(G_weighted, node) for node in G_weighted.nodes}

import pandas as pd

# Converting the shortest path dictionary to a DataFrame for better visualization
shortest_paths_df = pd.DataFrame(shortest_paths)

shortest_paths_df.to_csv("shortest_paths.csv", index=True)

print("Shortest Paths between All Vertices:\n", shortest_paths_df)
