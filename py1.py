from graf import Graph
from collections import deque

graph = Graph()
for node in ["A", "B", "C", "D", "E", "F", "G","H", "I","J"]:
    graph.add_node(node)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "E")
graph.add_edge("B", "F")
graph.add_edge("C", "F")
graph.add_edge("C", "G")
graph.add_edge("D", "H")
graph.add_edge("D", "I")
graph.add_edge("E", "J")
graph.add_edge("F", "J")

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.nodes[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, "A")

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph.nodes[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(graph, "A")


