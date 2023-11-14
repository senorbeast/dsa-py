## Unbounded Knapsack

## How ?
# Decision Tree, if we chose a particular item or not, recursively (for each item). 
# Till we reach the max capacity. (Capacity is reduced as we make decisions)
# All possible combinations, are taken into account, with the Decision Tree. 
#
# In Unbounded Knapsack, we can choose repeated items.


# Given a list of N items, and a backpack with a limited capacity, return the maximum total profit that
# can be contained in the backpack. The i-th item's profit is profit[i] and it's weight is weight[i].
# Assume you can have and unlimited number of each item available.


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

def dfs(profit, weight, capacity):
    return dfsHelper(0, profit, weight, capacity)

def dfsHelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0
    
    # Skip item i
    maxProfit = dfsHelper(i+1, profit, weight, capacity)

    # Include item i
    newCap = capacity - weight[i]
    if newCap >= 0:
        p = profit[i] + dfsHelper(i, profit, weight, newCap)  # Unbounded vs 0/1 Knapsack 
        # Compute the max
        maxProfit = max(maxProfit, p)

    return maxProfit

## Recursion with memoization (Top-Down DP as per Decision Tree)

# TC: O(n*m), SC: O(n*m)
# n -> no. of items, m -> capacity

def memoization(profit, weight, capacity):
    # A 2D array, with N rows and M + 1 columns, init -1's
    N, M = len(profit), capacity
    cache = [[-1] * (M + 1) for _ in range(N)]
    return memoHelper(0, profit, weight, capacity, cache)

def memoHelper(i, profit, weight, capacity, cache):
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

    return cache[i][capacity]
      

## DP (Bottom Up as per Decision Tree)
# TC: O(n * m), SC: O(n * m)
# Start by solving subproblems for smaller instances, (Top-Down in DP table)

# TODO: Try filling the DP table Bottom Up, (Top Down in Decision Tree)


def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column and row to reduce edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0]
    
    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i][c - weight[i]]
                dp[i][c] = max(include, skip)
    
    return dp[N-1][M]


## Space Optimized DP (Bottom Up)
# TC: O(n * m), SC: O(m)

def optimizedDp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [0] * (M + 1)  #prevRow

    for i in range(N):
        curRow = [0] * (M + 1)
        for c in range(1, M + 1):
            skip = dp[c]
            include = 0
            if c - weight[i] >= 0:
                include = profit [i] + curRow[c - weight[i]]
            curRow[c] = max(include, skip)
        dp = curRow

    return dp[M]