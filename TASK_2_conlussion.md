# Pathfinding in a Simplified City's Transportation Network using DFS and BFS

This project involves analyzing a simplified city's transportation network using Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to find paths between two specified stations. The graph representing the transportation network consists of 9 stations connected by 13 routes.

## Graph Representation

The graph is represented as follows:

**Stations (Nodes):**
- A, B, C, D, E, F, G, H, I

**Routes (Edges):**
- A-B, A-C, B-C, B-D, C-E, D-E, D-F, E-G, F-G, G-H, H-I, G-I, F-I

## Paths Found by DFS and BFS

**Starting Node:** A  
**Goal Node:** I

### Depth-First Search (DFS) Path
DFS explores as far as possible along each branch before backtracking. The path found by DFS is:
- A -> B -> C -> E -> D -> F -> G -> H -> I

### Breadth-First Search (BFS) Path
BFS explores all neighbors at the present depth before moving on to nodes at the next depth level. The path found by BFS is:
- A -> B -> D -> F -> I

## Comparison of DFS and BFS Paths

- **DFS Path:** A -> B -> C -> E -> D -> F -> G -> H -> I
- **BFS Path:** A -> B -> D -> F -> I

## Analysis

### Depth-First Search (DFS)
- **Characteristics:** DFS explores deeper into the graph by visiting child nodes before siblings.
- **Path Characteristics:** The path obtained by DFS is generally longer and may include backtracking as it prioritizes depth over finding the shortest path.
- **Reason:** In this implementation, DFS visits nodes alphabetically due to the nature of the graph traversal. It explores one entire branch before moving to another, leading to a longer and less direct path.

### Breadth-First Search (BFS)
- **Characteristics:** BFS explores all nodes at the present depth level before moving to the next level.
- **Path Characteristics:** The path obtained by BFS is typically shorter and more direct, as BFS finds the shortest path in an unweighted graph.
- **Reason:** BFS systematically explores all neighbors level-by-level, leading to a direct route from the start node to the goal node.

## Conclusion
- **DFS:** Suitable for scenarios where the complete exploration of all possible paths is required or when the graph is too large and deep to fit into memory.
- **BFS:** Ideal for finding the shortest path in an unweighted graph, making it more efficient for pathfinding in transportation networks.

By comparing the paths obtained using DFS and BFS, it is evident that BFS provides a more optimal and direct route, while DFS might explore more nodes and provide a longer path. The choice of algorithm depends on the specific requirements of the problem being solved.
