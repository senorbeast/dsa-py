#
# ### Graphs

# Prereq: LL, Trees
# Graphs are superset of LL, Trees

## For Graphs:
# 1. Node/Nodes are called Vertex/Vertices
# 2. Edges join two vertices
# 3. The structure can be connecte d in any way, not restricted like LL or Trees

# Only Restriction
# 4. E <= V^2           [Duplicate edges are not allowed]
#     - Every Vertex can have maximum V no. of Edges
#     - V Edges * V Vertex = V^2 Maximum Edges


## Types:
#
# 1. Directed Graph
#    Edges have only one direction
# 2. Undirected Graph:
#   Can travel through edges in both the direction


## Representation:

# 1. Matrix
# 2. Adjacency Matrix
# 3. Adjacency List


#%%
### Matrix
## Quiet Common

## TIP: Use variables rows and columns instead of x,y to avoid self-confusion
# rows increment in vertically, columns increment horizontally.


grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

# Here:
# Let
# 0 - Free
# 1 - Blocked

# Look at the Picture
# 0's Represent Nodes
# We can move up, down, right, left

#%%

## Adjacency Matrix
## Rarely Used

grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

## ! I have some doubt reading a Adjacency Matrix

# The indexes represent the Vertices
# 0 or 1 value represent the absence or present of edge.

## Disadvantages, uses a lot of spaces (space required to denote absense of edges)
## SC: O(v^2)


#%%

## Adjacency List

## Most Common
from typing import List


class GraphNode:
    def __int__(self, val: int):
        self.val = val
        self.neighbours: List[GraphNode] = []
