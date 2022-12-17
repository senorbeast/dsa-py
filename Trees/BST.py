##  Binary Search Tree

# A Binary Tree, with a sorted property (wierdly sortly). Similar required for Binary Search Algorithm (which is used for sorted arrays)

## Sorted Property:
# Every left child node, is less than its parent.
# Every right child node, is greater than its parent.

## For all BST:

# (Sorted Propert Implies):
# The Left most leaf is the min value of the whole tree
# The right most leaf is the max value of the whole tree

# Equal values? : Generally BST don't have duplicate values

# right sub tree (first right node and all its descendant)

## BST are recursive in nature,
## For a root node, its left node has A prop, right node has B property.
## This applies to all parent-child relationship. Thats why BST recursive in nation


#%%

from trees import TreeNode

# Start search with root node (We can do it will any node possibly)
def search(node, target):

    # Base case (null node, child of left node, doesn't exist)
    if not node:
        return False

    if target > node.val:
        return search(node.right, target)

    elif target < node.val:
        return search(node.left, target)

    else:
        return True


#%%

## Time Complexity:

# Balanced Tree: Height of left sub tree and right sub tree differ by 1.
# For Balanced tree: O(logn)
# For worst balanced tree: Well its a Linked list : O(n)

## Universally Time Complexity: O(h) : Where h is the height of the tree.


## Why we need BST?
# When we have Binary Search on Arrays

# Adding/Deleting to BST is easier O(logn). On Arrays its O(n) TC.
