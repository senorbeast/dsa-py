## Prim's Algorithm

## What?
# Greedily get MST from graph.
# Gives the minium spanning tree (MST), from an graph.
# 1. Can give cost of MST
# or 2. Find the MST  (There can exist multiple MST for a graph)

# MST: Acyclical, undirected, connected Graph with minimum total cost.
# For n nodes, to be connected in acyclic way, we will have n-1 edges.

## Why?
# Loads of applications

## Applications
# Finding optimal way to connect various cities in India
# Connecting Wired between components
# Connecting Entities with minimum connection length.

## How ?
# Basically a Dijkstra's Variation

## Steps
# Start with any node,
# 
# Visit (hashset): Don't visit same nodes again (to avoid cycles)
# 
# minHeap (<weight, n1, n2>): To get minium cost path
#
# Pop min edge from minHeap, add edges to minHeap
# Repeat

################## Dijkstra's vs Prims ########################
# In Prims
# Keeping track of src, dst for each edge, for the edges of MST
# [IMP] We don't add weights, since we don't want the path, we just want individual edges to connect all nodes.
# We are trying to minimize total edge cost for whole network, not thinking in term of a minimizing path cost from A to E 

## TC: 
# Worst Case: Adding E edges (E = V^2) to minHeap
# Adding 1 element to minHeap = log(E) 
# TC: O(E * log(V))


## Prims

from typing import List, Tuple
import heapq
import networkx as nx
import matplotlib.pyplot as plt


def primMST(edges: List[Tuple[int, int, int]], n: int) -> List[Tuple[int, int]]:
    # Create adjacency list
    adj: dict[int, List[Tuple[int, int]]] = {}  # {node: []}

    for i in range(1, n + 1):
        adj[i] = []
    for src, dst, weight in edges:
        adj[src].append((dst, weight))
        adj[dst].append((src, weight))

    # Prim's (Basically Dijkstras Variation)

    # Initialize the heap by choosing a single node
    # (in this case 1) and pushing all its neighbors.
    minHeap: List[Tuple[int, int, int]] = []  # cost, src, dst
    for neighbour, weight in adj[1]:
        heapq.heappush(minHeap, (weight, 1, neighbour))

    mst: List[Tuple[int, int]] = []  # list of edges
    visit: set[int] = set()
    visit.add(1)  # add 1st node

    while minHeap:
        weight, src, node = heapq.heappop(minHeap)
        if node in visit:
            continue

        mst.append((src, node))
        visit.add(node)

        for neighbour, weight in adj[node]:
            if neighbour not in visit:
                heapq.heappush(minHeap, (weight, node, neighbour))

    return mst



def highlight_mst_edges(edges: List[Tuple[int, int, int]], n: int, mst_edges: List[Tuple[int, int]]) -> None:
    G = nx.Graph()

    for s, d, w in edges:
        G.add_edge(s, d, weight=w)

    pos = nx.circular_layout(G)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black')

    # Highlighting the MST edges in green
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=2)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

    plt.title("Graph Visualization with Minimum Spanning Tree Highlighted")
    plt.show()

edges: List[Tuple[int, int, int]] = [(1, 2, 10), (1, 3, 5), (2, 3, 2), (2, 4, 1), (3, 2, 3), (3, 4, 9), (3, 5, 2), (4, 5, 4), (5, 4, 6)]
n: int = 5

# Prim's MST function
mst_edges = primMST(edges, n)

highlight_mst_edges(edges, n, mst_edges)