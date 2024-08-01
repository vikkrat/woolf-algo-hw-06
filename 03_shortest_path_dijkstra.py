import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))  # Для неорієнтованого графа

def dijkstra(graph, start):
    shortest_paths = {node: (float('inf'), None) for node in graph.nodes}
    shortest_paths[start] = (0, None)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > shortest_paths[current_node][0]:
            continue
        
        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            
            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, current_node)
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

def shortest_path(graph, start, end):
    shortest_paths = dijkstra(graph, start)
    path = []
    current_node = end
    
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][1]
        current_node = next_node
    
    path = path[::-1]
    return path, shortest_paths[end][0]

# Створення графа
G = Graph()
stations = ["Station A", "Station B", "Station C", "Station D", "Station E"]
for station in stations:
    G.add_node(station)

edges = [
    ("Station A", "Station B", 5),
    ("Station A", "Station C", 10),
    ("Station B", "Station D", 2),
    ("Station C", "Station D", 1),
    ("Station C", "Station E", 7),
    ("Station D", "Station E", 3)
]
for edge in edges:
    G.add_edge(*edge)

# Знаходження найкоротшого шляху та його довжини
shortest_path_result, shortest_path_length = shortest_path(G, "Station A", "Station E")
print("Найкоротший шлях за допомогою алгоритму Дейкстри:", shortest_path_result)
print("Довжина найкоротшого шляху:", shortest_path_length)
