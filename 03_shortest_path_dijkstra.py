import networkx as nx

G: nx.Graph = nx.Graph()
stations: list[str] = ["Station A", "Station B", "Station C", "Station D", "Station E"]
G.add_nodes_from(stations)

edges: list[tuple[str, str, int]] = [
    ("Station A", "Station B", 5),
    ("Station A", "Station C", 10),
    ("Station B", "Station D", 2),
    ("Station C", "Station D", 1),
    ("Station C", "Station E", 7),
    ("Station D", "Station E", 3)
]
G.add_weighted_edges_from(edges)

shortest_path: list[str] = nx.dijkstra_path(G, source="Station A", target="Station E")
shortest_path_length: int = nx.dijkstra_path_length(G, source="Station A", target="Station E")
print("Найкоротший шлях за допомогою алгоритму Дейкстри:", shortest_path)
print("Довжина найкоротшого шляху:", shortest_path_length)
