## Counting paths

## 2D Count paths
# Counts the number of unique paths from top left to bottom right, you are only allowed to move down or right.


### Why DP?
# Since we can divide the problem into smaller problems
# Since many parts of different paths will coincide.

arr = []

# %%

# Brute force DFS
# no. of rows = n
# no. of cols = m

# TC: O(2^(n+m))
# Every time the height of the recursive decision tree would be n+m
# So, the total no. of elements traverse would be 2^(n+m)

# SC: O(n+m)
# max length of callstack for recursive calls

def bruteForce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    
    return (bruteForce(r + 1, c, rows, cols) + bruteForce(r, c + 1, rows, cols))

print(bruteForce(0, 0, 4, 4))
#%%

# TC: O(n*m)    We sum up path count for each node once, then we just use cache.
# SC: O(n*m)    Cache

def memoBruteForce(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1

    cache[r][c] =  memoBruteForce(r + 1, c, rows, cols, cache) + memoBruteForce(r, c + 1, rows, cols, cache)

    return cache[r][c]

print(memoBruteForce(0, 0, 4, 4, [[0] * 4 for i in range(4)]))

# %%

## Bottom Up DP
# Easier when we understand the recursive way for it.
# Mathematically calculate, by referencing the recursive returns.
# May use maths tricks, more base condns. (More defined boundaries, to make the pattern of calc easier)
# Loop in reverse order, (BOTTOM-UP) 

# For this problem:
# By understanding the recursive way.
# We can deduce, that path count for a node, depends on 
#  1. node to the right
#  2. node to the left

# Writing out the recursive returns we understand
# last element of each row is always 1.
# we can get path count for a row of nodes, by path count of the row below.
# To start 
#   1. with we can take the out of bounds (imaginary row) to be filled with 0
#   2. set last element of row to 1
#   3. calc other element from the element below it (prevRow[c]), and to the right of it (currRow[c+1])

# Loop in reverse order, (BOTTOM-UP) for:
# (We calc element this, only for elements from the start, to the second last col, and till the last row.)
# Since, last col will always be 1.
# Last row, can depend on imaginary row [0, 0....]

# TC: O(n*m)  # Need to go through each element of matrix
# SC: O(m)    # Size of each row = no. of cols
def dpPathCount(rows, cols):

    # Imaginary row
    prevRow = [0] * cols

    for r in range(rows - 1, -1, -1):

        # Create empty currRow, except the last element will always be 1
        currRow = [0] * cols
        currRow[cols-1] = 1

        for c in range(cols - 2, -1, -1):
            # Fill the currRow accordingly
            currRow[c] = currRow[c + 1] + prevRow[c]
        
        # prepare for next iteration
        prevRow = currRow
    
    return prevRow[0]


print(dpPathCount(4,4))

# %%
