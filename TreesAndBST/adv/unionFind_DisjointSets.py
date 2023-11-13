#
## Union Find (Disjoint Sets)

# Forest of trees
# Multiple trees/graphs

## Advantages
# 1. Can deal with disjoint graphs
# 2. Can be used for cycle dectection

## Disadvanatage
## Doesn't accurately represent relationship between nodes.
# Its main use to find cyclicity

## Type: Union by Rank (height)
# While unionizing, try to keep the tree balanced. (For Better Efficiency)

# ----------------------------------------------------------------------------

# Q. Find cyclic or not

# edges = [[1, 2], [4, 1], [2, 4]]  # Bidirectional

## Solution
# Steps:

# 1. We have 4 single nodes
# 2. Assume they are initialize by themself.
# 3. Find the root of the nodes, unionize them .. (With Type Union By Rank)


## If new roots of both nodes are same, we have a cycle
# (If two nodes that are already connected, are reconnected, then we have a cycle)

## Rank = Height

# -------------------------------------------------------------------------------

#### Unionizing/ Cycle Dectection: With path compression and Balanced trees.

## TC: O(m)O(alpha(n) = O(m * alpha(n))    m = no. of edges
## Approximates to TC: O(m)O(1) = O(m)

## SC: O(n)                storing par, rank maps

## Union Find can be sometimes more efficient compare to DFS
## At 1. Cycle Detection
##    2. Counting no. of connected components


# The Union-Find data structure's optimized operations,
# including path compression and rank-based union,
# yield an amortized time complexity of approximately O(alpha(n)),
# where alpha(n) is the slow-growing inverse Ackermann function.
# This makes the structure highly efficient for most practical cases,
# though not truly constant time, due to the gradual growth of alpha(n).

# n: represent nodes/numbers from 1 to n
from typing import Dict

class UnionFind:
    def __init__(self, n:int) -> None:
        self.par: Dict[int, int] = {}  # Store Parent of each node
        self.rank: Dict[int, int] = {}  # Rank for each node

        for i in range(1, n + 1):
            self.par[i] = i  # For Root Node = Init its parent as itself
            self.rank[i] = 0

    # Find root node of tree
    # TC: O(height) = O(n)  [Max height = n, i.e. LL]

    ## With Optimization: path compression
    ## TC: O(logn)

    def find(self, n: int) -> int:
        p = self.par[n]

        # Find node before root node
        while p != self.par[p]:
            # Set child's parent directly to grandparent
            self.par[p] = self.par[self.par[p]]  # Optimization: path compressing

        return p

    # Unionize trees
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)

        # Same root nodes implies, cyclic tree (unionized tree)
        if p1 == p2:
            return False

        ## For more balanced trees
        # Shorter tree, will be attached to longer trees

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1  # Assign p1 as parent of p2

        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2  # Assign p2 as parent of p1

        else:
            self.par[p1] = p2
            self.rank[p2] += 1  # Inc height of p2 (Parent)

        return True
