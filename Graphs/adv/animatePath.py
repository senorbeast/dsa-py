import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from dijkstras_visualized import shortestPathWithPrev


def update(frame):
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black')
    labels = nx.get_edge_attributes(G, 'weight')

    # Highlight the edges in the current frame
    current_edge = shortest_path_edges[frame]
    nx.draw_networkx_edges(G, pos, edgelist=[current_edge], edge_color='green', width=5)
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
    plt.title("Graph Visualization with Equal Edge Lengths and Animated Shortest Path")

edges = [(1, 2, 10), (1, 3, 5), (2, 3, 2), (2, 4, 1), (3, 2, 3), (3, 4, 9), (3, 5, 2), (4, 5, 4), (5, 4, 6)]
n = 5
src = 1

shortest_path_result = shortestPathWithPrev(edges, n, src)
print("Shortest Path:", shortest_path_result)

G = nx.DiGraph()
for s, d, w in edges:
    G.add_edge(s, d, weight=w)

pos = nx.circular_layout(G)
shortest_path_edges = [(shortest_path_result[node][1], node) for node in shortest_path_result if node != src]

# Set up animation
num_frames = len(shortest_path_edges)
animation = FuncAnimation(plt.figure(), update, frames=num_frames, interval=1000, repeat=False)

plt.show()