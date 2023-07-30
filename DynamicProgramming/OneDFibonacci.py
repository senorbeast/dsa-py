# For 1D Dynamic Programming

# Breaking into small problem
# Most DP, problems can be represented in equation

# Fibonacci

# Base case: F(0) = 0, F(1) = 1
## Big problem = F(sub problems)
# F(n) = F(n-1) + F(n-2)

#%%

# To get the nth Fibonacci Number

# Brute Force
def recurseFibo(n: int) -> int:
    if n <= 1:
        return n
    return recurseFibo(n - 1) + recurseFibo(n - 2)


# Coincidence or logic n = Height of the tree. ? [LOGIC]
# Height of tree  = n
#         5
#     4       3
#   3   2    2   1
#  2 1 1 0  1 0
# 1 0

# Height of tree = n
#            6
#          5   4
#        4  3  3  2
#      3  2 2 1 2 1  1 0
#     2 1 11 11  11
#    1 1

## No. of elements in tree = 2^n
## Height : n
# A lot repeated work
## TC: O(2^n)

#######################################################

# We can optimize this, with help of a technique in Dynamic Programming

## Memoization
#%%

# TC: O(n)
# Only n elements are required to be calculated,
# from the binary tree of recursion. Rest will be cached.
# (See the tree example above)

# SC: O(n) [Caching n-1 values]


def memoizedRecursionFibo(n: int) -> int:

    cache = {}

    # Check cache
    if n in cache:
        return cache[n]

    # cache the res, then return
    cache[n] = recurseFibo(n)
    return cache[n]


## Repeation is avoided.
# But some SC is increased.


for i in range(10):
    print(i, ":", memoizedRecursionFibo(i))


# Also refered as Top Down DP.
# Since, we are going from Top and recursing down, the tree


################################################################

## Bottom Up Approach

# Basically, divide the problem, into sub problems and work upwards.
# We are goint to start in bottom and work our way upward
## Sometimes called TRUE DP.

# %%

# TC: O(n)
# SC: O(1)

# Find Fibo at nth position
def FiboDP(n):
    if n < 2:
        return n

    # Sub array
    dp = [0, 1]
    i = 2

    # Start from i, go adding till n
    # Loop over till we reach n (higher value)
    while i <= n:
        # Optimized to use on 2 positions in array
        ## SC: O(1), Space Complexity doesn't scale with input size. Its fixed to 2.
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1

    return dp[1]


print(FiboDP(5))


# %%
for i in range(10):
    print(i, ":", FiboDP(i))
