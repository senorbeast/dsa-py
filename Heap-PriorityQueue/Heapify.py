## Heapify or Build Heap.

# Input: We are given values in an array.

# Output: We can turn them into a Heap/Priority Queue form
# Which will follow the Structure and Order Properties in TC: O(n)

## Its easy to follow the Structure Property TC: O(1):
# (Only leaf layer can have empty nodes)
# Just an array, with the 1st element with a dummy value:
# Add a dummy value at the end.
# And swap the 1st ele, with the last ele (dummy # Percolate down, (for all parent node)


## For Order Property
# (Every child value must be greater than its parent value (min heap))

# Percolate down, (for all parent node)


## TC: O(n)

## Can't percolate down on leaf nodes anyway.
## No, need to percolate over half the elements in tree.

# (For complete tree)
# n = 1 + 2 + 4 + 8
# n = 15

#              14                                ## 1 ele           ~ n/16 else
#         19         16                          ## 2 ele           ~ n/8 eles
#      21    26    19   68                       ## 4 ele           ~ n/4 eles
#    65 30                                       ## 8 ele max       ~ n/2 eles

# No. of Operations, for percolating down
# For bottom layer we get:  O(n/2 * 0)
# For bottom - 1 layer we: O(n/4 * 1)
# ....
# Total TC: O(n/2 * 0 + n/4 *1 + n/8 * 2 ....  + 1 * h)
# No. of terms in the summation ~ = height of tree.
# Summation = n( 1/(2^k) * i)
## Total TC: O(n)


## IMPORTANT:
# Although we can build a heap with this method in O(n) TC.
# Sorting an random array will require,
# 1. Building a heap/priority queue first ## O(n)
# 2. Popping the min value                ## O(logn)
## So, sorting an random array with heap/priority queue is also O(nlogn)
