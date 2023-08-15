
# Find the length of the shortest path from the top left of the grid to the bottom right

# BFS:
# Layer by layer
#%%

# n = number of elements in matrix
# TC: O(n)   (We don't visit same element twice)
# SC: O(n)

# Shortest path from top left to bottom right

from collections import deque

# Returning length of shortest path in grid

# The number of layers in BFS traversal give the lengths

# ⭐⭐ Branches in path, (children of tree) are added to the queue as usual in BFS
# We don't traverse the same node again, so immediately add to visit, once added to queue
# Since in Graphs, a node can be pointed by multiple nodes

## ⭐ Why no. of levels gives us the shortest path to a node?

# We don't visit the same element twice, because, if its already visited, 
# we have reached it in a prev level or same level (We already have the shortest path to the node)

## ⭐ Every new level, we get the shortest path to those nodes

## We keep counting the no. of levels of the traversal with BFS
# Whenever we reach the target node, we return the length

## Its the most efficient way to get the shortest path, since we only visit each element onces
# and return as soon as we reach the solution


def bfs(grid: list[list[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visit =  set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0,0))

    length = 0

    while queue:
        # len(queue) acts as snapshot for length of queue in current level
        for _ in range(len(queue)):
            r, c = queue.popleft()

            # Reached Target!!
            if r == ROWS - 1 and c == COLS - 1:
                return length
            

            # Go through all 4 directions
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]] # basically the directions to next node
            
            for dr, dc in neighbors:
                # Out of bounds, already visited, blocked
                if (r + dr < 0 or c + dc < 0 or 
                    r + dr == ROWS or c + dc == COLS or 
                    (r + dr, c + dc ) in visit or 
                    grid[r + dr][c + dc] == 1):
                    continue
                
                # Reached next valid position
                # All valid children nodes will be appended to the queue and added to visited.
                queue.append((r + dr, c + dc)) # Next layer.
                visit.add((r + dr, c + dc)) # Never visit same cell twice
    
        length += 1

    return -1  # No Solution

