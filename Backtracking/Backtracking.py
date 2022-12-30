# Backtracking


# Kind of a brute force approach, in which we backtracking from our mistake and try out another way.

# Question:
#
# Determine if a path exist from the root of the tree to a leaf node, without any 0s in the path.
# Return true if true.


#     4
#  0     1
#   7   2 0


# Here, only valid path is 4 -> 1 -> 2

## Since here, we have to go through every pos, then we may need to backtrack.


#%%

# Can we reach leafNode without any value 0 in path
from TreesAndBST.trees import TreeNode


def canWeReachLeaf(root: TreeNode | None):
    # Base Condn
    if not root or root.val == 0:
        return False

    # If leaf node (another Base Case)
    if not root.left and not root.right:
        return True

    if canWeReachLeaf(root.right):
        return True

    if canWeReachLeaf(root.left):
        return True

    return False


#%%

# Show the path, for non-zero connect between root and leaf node

# Lets assume only 1 path exists atmost


def leafPath(root, path):

    if not root or root.val == 0:
        return False

    path.append(root.val)

    if not root.left and not root.right:
        return True

    if leafPath(root.left, path):
        return True

    if leafPath(root.right, path):
        return True

    # Ifs any sub tree is not true
    # We backtrack
    path.pop()

    return False  # Goes to the parent recurse call, and proceeds.


#%%
# TC: O(n) worst case runs over all nodes.
