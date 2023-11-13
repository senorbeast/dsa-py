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

from TreesAndBST.adv.unionFind_DisjointSets import UnionFind


def minimumSpanningTree(edges: List[Tuple[int, int, int]], n: int) -> List[Tuple[int, int]]:

    minHeap: List[Tuple[int, int,int]] = [] # cost, src, dst
    
    for n1, n2, weight in edges:
        heapq.heappush(minHeap, (weight, n1, n2))

    unionFind = UnionFind(n)
    mst = []

    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(minHeap)
        if not unionFind.union(n1, n2):
            continue
        mst.append((n1, n2))

    return mst
