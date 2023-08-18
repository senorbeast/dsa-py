#%%
# GraphNode used for adjacency list

from collections import deque
from typing import Dict, List


class GraphNode:
    def __init__(self, val) -> None:
        self.val  = val
        self.neighbours = []

### Usually we use HashMap to Represent an Adjacency List Graph


adjList: Dict[str, List[str]] = {"A": [], "B": []}

# ----------------------------------------------------------------
#%%
### Given directed edges, build an adjacency list

# A-> B 
edges: List[List[str]] = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

## HashMap of List for Graphs is Adjcency List
adjList: Dict[str, List[str]] = {}

for src, dst in edges:
    # Add empty list, if not init
    if src not in adjList:
        adjList[src] = [] 
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

print(adjList)
#%%
#------------------------------------------------------------------

# Count paths (backtracking)
#
# Backtracking: 
#  - Keep track of visited List
#   - :star: For more paths, remove current node from visited list,
#   so its sibling in the stack call, (parent's another child in callstack)
#   can go through the node.

#   Basics:
#   - Return 1 for succesfull path
#   - Recursively DFS for each node, pass along visited list

# n : no. of nodes / vertices
# h : height of decision tree, hmax = n
# e : no. of branches/ no. of edges

# TC: O(e^h) 
# SC: O(n)  # Visited memoization

# If not using visited memoization
# TC: O()

## TC: 
#
def dfs(node, target, adjList, visit):

    # Base Condn
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    
    # After getting count for current node, 
    # remove this node from visited, so parent from callstack
    # can call another child function call. (Sibling for current node)
    # And it would be able to access path of this node.

    visit.remove(node)

    return count


#----------------------------------------------------------------------

## Shortest path from node to target

# For non-overlapping vertex in single path we require visited node.
# We don't want to go up in the tree, or get stuck in a cycle

# The height of the graph/tree, gives us the shortest path

# v = no. of vertices
# e = no. of edges
# e <= v^2 

# TC: O(v+e)
# SC: O(2v) = O(v)

# BFS visits each node once, enqueueing and dequeueing in proportion to the number of nodes (O(V)).
# Exploring neighbors involves traversing edges, each visited once due to adjacency list, making the complexity O(E).
## each edge is visited only once, not for each vertex.  
# Thus, overall BFS time complexity is O(V + E).

def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    while queue:

        # For vertex/nodes in single level
        for _ in range(len(queue)):
            # Each Node
            curr = queue.popleft()
            if curr == target:
                return length

            for neighbor in adjList[curr]:
                # Neighbor for each node
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length