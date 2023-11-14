## Kruskal

# Greedily get MST from graph.

# Prim's alternative, easier to understand, but a bit difficut to implement due to Union Find

# Same logic as Prims
# Take minimum edges, being greedy. 
# But

# We take all edges, pick shortest/cheapest edge. Unionize nodes with that edge.
# Take next cheapest edge, beware of cycles (union find will tell us) then unionize nodes
# Do this until we have n - 1 edges 


# Given an list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minium spanning tree.

# TC: O(E * log(V))
# SC: O(E)

import heapq
from typing import List, Tuple
from prims import highlight_mst_edges 

from TreesAndBST.adv.unionFind_DisjointSets import UnionFind


def kruskalMST(edges: List[Tuple[int, int, int]], n: int) -> List[Tuple[int, int]]:
    """ Kruskal Algorithm to find minimum spanning tree, from a graph of nodes
        
        # TC: O(E * log(V))
        # SC: O(E)

    Args:
        edges (List[Tuple[int, int, int]]):  Edges for the Graph Input (src, dst, weight)
        n (int): No. of nodes

    Returns:
        List[Tuple[int, int]]: Edges for MST
    """

    minHeap: List[Tuple[int, int,int]] = [] # cost, src, dst
    
    # Create complete minHeap (SC: O(E))
    for n1, n2, weight in edges:
        heapq.heappush(minHeap, (weight, n1, n2))

    unionFind = UnionFind(n)
    mst = []

    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(minHeap)                        # TC: O(logV)
        if not unionFind.union(n1, n2):  # if already unionized        # TC: O(n) or O(1)   
            continue
        mst.append((n1, n2))

    return mst


edges: List[Tuple[int, int, int]] = [(1, 2, 10), (1, 3, 5), (2, 3, 2), (2, 4, 1), (3, 2, 3), (3, 4, 9), (3, 5, 2), (4, 5, 4), (5, 4, 6)]
n: int = 5

# Prim's MST function
mst_edges = kruskalMST(edges, n)

highlight_mst_edges(edges, n, mst_edges)
