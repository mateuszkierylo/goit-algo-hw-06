import networkx as nx
import matplotlib.pyplot as plt

# Create a graph representing a simplified city's transportation network
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

# Analyze the main characteristics
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_vertices = dict(G.degree())

# Plotting the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold', edge_color='gray')
plt.title("Simplified City's Transportation Network")
plt.show()

num_vertices, num_edges, degree_of_vertices
