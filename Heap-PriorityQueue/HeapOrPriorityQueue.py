## Heap or Priority Queue

## Why we need it?
# 1. To find min/max value as fast as possible. TC: O(1)
# For BST min/max reqs TC: O(logn)

# 2. Building them is Time efficient.
# Heaps, inserting each value TC: O(logn), for n values TC: O(nlogn)
# Special algorithm to build a Heap/Priority queue:

# BST, we insert a node every time.  TC: O(logn)
# For full BST with len n.  TC: O(nlogn)

## Disadvantage:
# Searching is ## TC: O(n)
# BST Searching ## TC: O(logn)

## Coding Interviews, Heaps/Priority Queue are used a lot.
## We need to use min/max value a lot.
# Heapify TC: O(n)
# Push/Pop TC: O(logn)
# Find Min/Max TC: O(1)

## What is heap?
# Simple: Priortize min/max values
# Interface as per a Queue, but under the hood its a Heap.


# Here Priority Queue, is implemented with a Binary Heap (min or max)
# Heaps can have duplicates (which Binary Trees can't have)

#              14                                ## 1 ele
#         19         16                          ## 2 ele
#      21    26    19   68                       ## 4 ele
#    65 30                                       ## 8 ele max


## Properties
# 1. Structrue property
#  Only last layer may have any missing nodes
#  And Nodes must be added from left to right, which will bring empty nodes to the right.

# 2. Order property
# Recursively, root node must be greater than both its sub trees.
# So min value is the root node ## For max heap, we would want smaller instead of greater.


## Although Binary Heaps can look like binary trees, they are implemented as an array.
## And we don't start at zeroth index. (To get the maths to work out)
## Root is always at index node.
## next we fill in 19 at index 2. 16 at index 3, and so on.

arr: list[int] = [0, 14, 19, 16, 21, 26, 19, 68, 65, 30]
# left child = 2*i
# right child = 2*i  + 1
# parent  = i/2              (floor division)

## These properties are true since, they follow the Structure property, without any holes.

## Percolating Down is better than Percolating Upward.
# Since, at max the root will be percolate down through logn height of tree.
# But, in percolating up, the bottom layer which is wider. will be percolating up the logn height.
## More elements to percolate up, than in percolating down.
