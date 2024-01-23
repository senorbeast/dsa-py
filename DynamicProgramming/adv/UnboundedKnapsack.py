## Unbounded Knapsack

## Question
# Given a list of N items, and a backpack with a limited capacity, return the maximum total profit that
# can be contained in the backpack. The i-th item's profit is profit[i] and it's weight is weight[i].
# Assume you can have and unlimited number of each item available.

## How ?
# Decision Tree, if we chose a particular item or not, recursively (for each item). 
# Till we reach the max capacity. (Capacity is reduced as we make decisions)
# All possible combinations, are taken into account, with the Decision Tree. 
#
# In Unbounded Knapsack, we can choose repeated items.

## Decision Tree
# Organize the Decision Tree, then we know, which subproblems are solve by which section of tree.
# For Unbounded Knapsack the decision tree size will be large. (because of repeats)

## Two ways:
# 1. Binary Decision Tree
# 2. Multiple children Decision Tree


## STEPS:

# 1. Decision Tree
# 2. Recursive (Brute Force)
# 3. Recursive Memoized
# 4. DP (iterative with dp table)
# 5. Space Optimized DP (iterative with much smaller dp table)

## Brute Force, Recursion (Decision Tree)
## TC: O(2^c), SC: O(c)
# c -> capacity

from typing import List


def dfs(profit: List[int], weight: List[int], capacity: int) -> int:
    return dfsHelper(0, profit, weight, capacity)

def dfsHelper(i: int, profit: List[int], weight: List[int], capacity: int) -> int:
    # Base Case, we go out of bounds of the profit index
    if i == len(profit):
        return 0
    
    # Skip item i
    skip = dfsHelper(i+1, profit, weight, capacity)
    
    include = 0
    # Include item i
    newCap = capacity - weight[i]
    if newCap >= 0:
        include = profit[i] + dfsHelper(i, profit, weight, newCap)  # Unbounded vs 0/1 Knapsack 
        # include = profit[i] + dfsHelper(i + 1, profit, weight, newCap) # For 0/1 Knapsack (can't repeate items), next item (i + 1)

    # Choose the branch based on max profit
    return max(skip, include)


## Recursion with memoization (Top-Down DP as per Decision Tree)

# TC: O(n*m), SC: O(n*m)
# n -> no. of items, m -> capacity
# SC: Cache size, n*m 

def memoization(profit: List[int], weight: List[int], capacity: int) -> int:
    # A 2D array, with N rows and M + 1 columns, init -1's 
    # Rows: Items index (O to N-1) give N rows
    # Column: Capacity (0 to M) give M + 1 columns

    N, M = len(profit), capacity
    cache = [[-1] * (M + 1) for _ in range(N)]

    # Print the initial state of the cache
    print("Initial Cache:")
    for row in cache:
        print(row)

    return memoHelper(0, profit, weight, capacity, cache)

def memoHelper(i: int, profit: List[int], weight: List[int], capacity: int, cache: List[List[int]]) -> int:
    if i == len(profit):
        return 0
    if cache[i][capacity] != -1:
        return cache[i][capacity]
    
    # Skip item i
    cache[i][capacity] = memoHelper(i + 1, profit, weight, capacity, cache)

    # Include item i 
    newCap = capacity - weight[i]
    if newCap >=0:
        p = profit[i] + memoHelper(i, profit, weight, newCap, cache)
        # Compute the max
        cache[i][capacity] = max(cache[i][capacity], p)
    
    # Print the state of the cache after each recursive call
    print(f"\nCache After Recursive Call ({i}, {capacity}):")
    for row in cache:
        print(row)


    return cache[i][capacity]
      

## DP (Bottom Up as per Decision Tree)
# TC: O(n * m), SC: O(n * m)
# Start by solving subproblems for smaller instances, (Top-Down in DP table)

# TODO: Try filling the DP table Bottom Up, (Top Down in Decision Tree)

def dp(profit: List[int], weight: List[int], capacity: int) -> int:
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column and row to reduce edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = (c // weight[0]) * profit[0] 
    
    # Print the initial state of the DP table
    print("Initial DP Table:")
    for row in dp:
        print(row)
    
    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i][c - weight[i]]
            dp[i][c] = max(include, skip)
        
        # Print the state of the DP table after each iteration
        print(f"\nDP Table After Iteration {i}:")
        for row in dp:
            print(row)
    
    return dp[N-1][M]


## Space Optimized DP (Bottom Up)
# TC: O(n * m), SC: O(m)

def optimizedDp(profit: List[int], weight: List[int], capacity: int) -> int:
    N, M = len(profit), capacity
    dp = [0] * (M + 1)  #prevRow

     # Print the initial state of the DP table
    print("Initial DP Table:")
    print(dp)

    for i in range(N):
        curRow = [0] * (M + 1)
        for c in range(1, M + 1):
            skip = dp[c]
            include = 0
            if c - weight[i] >= 0:
                include = profit [i] + curRow[c - weight[i]]
            curRow[c] = max(include, skip)
        
        # Print the state of the DP table after each iteration
        print(f"\nDP Table After Iteration {i}:")
        print(curRow)

        dp = curRow

    return dp[M]


# Call the function with your input
profit = [1, 2, 5]
weight = [1, 2, 3]
capacity = 5

result = dfs(profit, weight, capacity)
print(f"\nMaximum Profit Recursion: {result}")


# resultM = memoization(profit, weight, capacity)
# print(f"\nMaximum Profit Memoized Recursion: {resultM}")

resultDP = dp(profit, weight, capacity)
print(f"\nMaximum Profit DP: {resultDP}")

resultODP = optimizedDp(profit, weight, capacity)
print(f"\nMaximum Profit Optimized DP: {resultODP}")
