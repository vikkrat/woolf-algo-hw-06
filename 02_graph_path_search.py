import networkx as nx
from typing import Generator, List

G: nx.Graph = nx.Graph()
stations: list[str] = ["Station A", "Station B", "Station C", "Station D", "Station E"]
G.add_nodes_from(stations)

edges: list[tuple[str, str]] = [
    ("Station A", "Station B"),
    ("Station A", "Station C"),
    ("Station B", "Station D"),
    ("Station C", "Station D"),
    ("Station C", "Station E"),
    ("Station D", "Station E")
]
G.add_edges_from(edges)

def dfs_paths(graph: nx.Graph, start: str, goal: str) -> Generator[List[str], None, None]:
    stack: list[tuple[str, list[str]]] = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

dfs_path: list[list[str]] = list(dfs_paths(G, "Station A", "Station E"))
print("Шляхи за допомогою DFS:", dfs_path)

def bfs_paths(graph: nx.Graph, start: str, goal: str) -> Generator[List[str], None, None]:
    queue: list[tuple[str, list[str]]] = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

bfs_path: list[list[str]] = list(bfs_paths(G, "Station A", "Station E"))
print("Шляхи за допомогою BFS:", bfs_path)

print("Шляхи за допомогою DFS:", dfs_path)
print("Шляхи за допомогою BFS:", bfs_path)
