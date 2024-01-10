## Longest Common Subsequence

## Common Problem

# Terminology
# Subsequence: In order, non contiguous are fine
# Subarray: In order, contiguous elements
# Subset: Order doesn't matter, non contiguous are fine

# Question
## Given two strings s1 and s2, find the length of 
# the longest common subsequence between the two strings.

s1 = ["A", "D", "C", "B"]
s2 = ["A", "B", "C"]

# Steps:

# Try to divide into subproblems
# Here subproblems are LCS(smaller strings)
# End case is index out of bounds for any 1 or both strings

# LCS(string) = 1 + LCS(smaller string)

# Decision tree
#                                            (A,A)          + 1
#                                       i1 = 0, i2 = 0                      A = A  # char matches, for next problem both strings are reduced
#                                            (D,B)                                        
#                                       i1 = 1, i2 = 1                      D != B # no match, decision tree branches
#                                  (D,C)                   (C,B)                                 
#                           i1 = 1, i2 = 2         i1 = 2, i2 = 1                   
#                     (C,C)  +1      (D,OFB)      (B,B)   +1       (C,C)  +1                 
#                 i1 = 2, i2 = 2    i1=1, i2=3    i1=3, i2=1    i1 = 2, i2 = 2
#                                                                 (B, OFB)
#                     ....                                     i1 = 3, i2 = 3    (Out of Bounds: Base Case)

# max total of LCS = 2 

# No. of nodes in Decision Tree: 
# (Worst case: 2 branchs at each level)

# No. of nodes: n = 2^(l1 + l2)
# Height of Decision Tree: l1 + l2


# l1 = 2, l2 = 2

##          (0,0)
##        (0,1) (1,0)
##      (0,2) (1,1) (2,0)(1,1)
##     OFB   (2,1) (1,2) (3,1) (2,1) (2,1)(1,2)     (All are OFB)