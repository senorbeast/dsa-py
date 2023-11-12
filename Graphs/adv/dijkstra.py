## Dijkstra's Algorithm

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

# Size of minHeap = Edges in the graph = V^2 (Worst case)
# push/pop from heap for each edge => log(E) operations

# For E edges, E.log(E) operations

# TC for Dijkstra's:
# O(E.log(E)) 
#     or 
# O(E * log(V))            [With worst case of edges, in the minHeap]


## Given a connected graph represented by a list of edges, where 
# edge[0]

 
