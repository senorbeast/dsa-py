##
## Matrix DFS

## DFS and backtracking have a lot of overlap

# Q: Count the unique paths from the top left ot the bottom right.
# A single path may only move along 0's and can't visit
# the same cell more than once.

## Solution:
'''
We can only travel through the 0s and cannot revist a 0 for a single path

Backtracking/ DFS with recursion


In the callstack, its a stack, that traverses a tree in DFS manner

⭐ ⭐ ⭐ Its Backtracking,
once a child call "returns" control to the parent,
then the parent calls its other children. This way covering a new path.
(the other tracks will be call by the parent)

'''
#%%

# Count paths (backtracking)


from typing import List


# Recursive traverse the Matrix in (DFS manner), return 1 when a path reaches the target destination

def dfs(grid: List[List[int]], r: int, c: int, visit: set[tuple[int,int]]) -> int:

    ROWS, COLS = len(grid), len(grid[0])

    # Base condn
    # 1. r, c out of bounds
    # 2. Node already visited
    # 3. Path is blocked
    if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
        return 0
    
    # Base condn
    # Reached Target!!
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    # Keep track of visited nodes, to avoid revisiting it 
    visit.add((r, c))  #hashset

    count = 0

    # For a particular node, we can move in all 4 directions, base condn with check if its not possible
    # So, create recursive calls for each
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    ## Once return for a node is received
    # Since that would be the leaf node/ base condn has being reach for that node.
    # We have found a unique path, or we are at a dead end
    # Control is "returned" to the parent, 
    # and it will call other children, which would be other paths. 
    # Delete current node (current child), so it can be revisited by other paths.

    # OR

    ## ⭐ Parent recursive call will still be in callstack (and it will call its other children (other paths)), 
    # We would return control to the parent call by "return x", 
    # and other children of the parent, can be visiting this node again. (So delete this node from visit (current child)) 
    # Since those paths/subpaths would be unique, (we are yet to traverse them).

    # visit is passed by address.

    visit.remove((r, c))

    return count

#%%
grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
print(dfs(grid, 0, 0, set()))