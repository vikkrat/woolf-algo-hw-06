import networkx as nx
import matplotlib.pyplot as plt

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

pos: dict[str, tuple[float, float]] = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь кожної вершини:", dict(G.degree()))
