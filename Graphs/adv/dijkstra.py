## Dijkstra's Algorithm

# Greedy Alg, just like Prims, Kruskals

## What ?
# Dijkstra's is a shortest path algo, gives shortest path to every node, from the root node.

## Why?
# BFS works for unweighted graph, but for weighted graph we require Dijkstra's Algorithm
# BFS goes layer by layer, doesn't look at weights, Dijkstra's is a "Greedy" BFS which takes weights into account for greediness.

## How ?

# minHeap with key as the cost of edges

# Steps
# 1. Start from the root node, visit its neighbours. Update minHeap, with the nodes edges.
# 2. Go to the node at top of minHeap. Update minHeap, with the nodes edges, add prev node's cost.
# 3. The resultant cost of each node from start, will be given by key of minHeap.

# This works because we have the minHeap always giving us the cheapest/shortest path to traverse, to visit each node from the start.

## Problem
# Starting from A, find the length of the shorted path to every other node.
# A, B, C, D, E
# 0     3

## TC: 
# V -> vertices of the graph;
# E -> edges of the graph;  E <= V^2

# Size of minHeap = Edges in the graph E = V^2 (Worst case)
# push/pop from heap for each edge => log(E) operations

# For E edges, E.log(E) operations

# TC for Dijkstra's:
# O(E.log(E)) 
#     or 
# O(E * log(V))            [With worst case of edges, in the minHeap]


## Given a connected graph represented by a list of edges, where 
# edge[0] = src, edge[1] = dst, and edge[2] = weight, 
# find the shortest path from src to every other node in the graph.
# There are n nodes in the graph.
# O(E*log(V))

#%%
# Dijkstra's Algo
from typing import List, Tuple, Dict
import heapq

def shortestPath(edges: List[Tuple[int, int, int]], n: int, src: int) -> Dict[int, int]:

    # Converting edges to adj list
    adj: Dict[int, List[Tuple[int, int]]] = {}
    for i in range(1, n + 1):
        adj[i] = []

    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append((d, w))

    # Dijkstra's
    shortest: Dict[int, int] = {}
    minHeap: List[Tuple[int, int]] = [(0, src)]

    while minHeap:
        # Got shortest path for node (if new node)
        w1, n1 = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        # For neighbours of n1
        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, (w1 + w2, n2))

    return shortest

#%%

edges = [(1, 2, 10), (1, 3, 5), (2, 3, 2), (2, 4, 1), (3, 2, 3), (3, 4, 9), (3, 5, 2), (4, 5, 4), (5, 4, 6)]
n = 5 # Number of nodes
src = 1 # Source node
result = shortestPath(edges, n, src)
print(result)

