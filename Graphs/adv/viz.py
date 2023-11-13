import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
import heapq


def shortestPathWithPrev(edges: List[Tuple[int, int, int]], n: int, src: int) -> Dict[int, Tuple[int, int]]:

    # Converting edges to adj list
    adj: Dict[int, List[Tuple[int, int]]] = {}
    for i in range(1, n + 1):
        adj[i] = []

    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append((d, w))

    # Dijkstra's
    shortest: Dict[int, Tuple[int, int]] = {} # {node: (cost, prevNode)}
    minHeap: List[Tuple[int, int, int]] = [(0, src, src)]  # (cost, node, prevNode)
    # Since heapq function uses the first key to sort/update minHeap.

    while minHeap:
        # Got shortest path for node (if new node)
        w1, n1, prev = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = (w1, prev)

        # For neighbors of n1
        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, (w1 + w2, n2, n1))

    return shortest


def visualize_graph_equal_length(edges, n, shortest_path_result):
    G = nx.DiGraph()

    for s, d, w in edges:
        G.add_edge(s, d, weight=w)

    pos = nx.circular_layout(G)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black')

    # Highlighting the shortest path in green
    shortest_path_edges = [(shortest_path_result[node][1], node) for node in shortest_path_result if node != src]
    nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='green', width=2)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

    plt.title("Graph Visualization with Equal Edge Lengths and Shortest Path Highlighted")
    plt.show()

# # Example usage
# edges = [(1, 2, 10), (1, 3, 5), (2, 3, 2), (2, 4, 1), (3, 2, 3), (3, 4, 9), (3, 5, 2), (4, 5, 4), (5, 4, 6)]
# n = 5
# src = 1

# shortest_path_result = shortestPathWithPrev(edges, n, src)
# print("Shortest Path:", shortest_path_result)

# visualize_graph_equal_length(edges, n, shortest_path_result)
