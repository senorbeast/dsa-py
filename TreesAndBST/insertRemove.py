## Advantage of BST over, Binary Search on sorted Arrays.
# 1. Insert/Remove takes O(logn), instead of O(n)
# For balanced BST.

# AVL Tree: For better balanced tree (Adv Alg)


#%% Insert node into BST
from trees import TreeNode


def insert(root: TreeNode | None, val: int):

    # no child exist
    if not root:
        return TreeNode(val)

    # Traverse down recursively to proper node of the tree by comparing, till we reach the leaf.
    # Then insert function returns the Treenode with value,
    #  which we assign, to the left/right child accordingly.
    # Then we return this update node (sub-tree), to prev insert call in the recurse stack.
    # Which will be assigned to root.right or left (but its not necessary since we will be mutating in place.)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)

    return root


#%% Create BST

# To find the node, tranverse the tree (logn Time Complexity)
# Time Complexity: O(logn)

newTree = TreeNode(20)
insert(newTree, 5)
insert(newTree, 3)
insert(newTree, 1)
insert(newTree, 23)
insert(newTree, 24)
insert(newTree, 30)
insert(newTree, 12)
insert(newTree, 6)
insert(newTree, 26)
insert(newTree, 8)
insert(newTree, 10)
insert(newTree, 16)
insert(newTree, 38)
insert(newTree, 40)
insert(newTree, 36)
insert(newTree, 34)
insert(newTree, 32)


#%% Print Inorder

from DFSforBST import inorder, reverseOrder

inorder(newTree)
#%%
reverseOrder(newTree)

# %%

## BST Remove


def minValueNode(root: TreeNode) -> TreeNode:
    curr = root

    # Till left child exists
    while curr and curr.left:
        curr = curr.left

    return curr


## There are 2 cases ,for removing a node

# The node we are removing has:
# Case 1: 0 or 1 child
# Case 2: 2 children


def removeNode(root: TreeNode | None, val: int) -> TreeNode | None:

    # No matching node
    if not root:
        return None

    # Get to the node
    if val > root.val:
        root.right = removeNode(root.right, val)
    elif val < root.val:
        root.left = removeNode(root.left, val)
    else:
        # Got the node
        # Since we are recursively finding and returning
        # Now root will be the correct node. (i.e. root.val = val)

        # If left child doesn't exist, return the right child to parent of correctnode.
        # * (grandparent will recieve their grandchild. (This way parent will be delete.))
        # * Parent is skipped, Since now grandparent, connects directly to their only grandchild.

        # Case 1 ( 0 or 1 child exist)
        if not root.left:
            # will return this to parent, recursively
            # will return null, if right child also doesn't exist.
            return root.right

        elif not root.right:
            return root.left

        else:
            # Case 2 (both child exist)

            # * Parent needs to replaced. But by which child??
            # * To maintain BST properties.

            #    Parent can be replaced, by min node, of its right sub tree
            # OR                         by max node, of its left sub tree.
            # Since they will be the most closest value to the correct node. And won't distrub the BST Sortted propery.

            # Then delete that leaf node. (min/max of that sub tree)

            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = removeNode(root.right, minNode.val)
        return root


#%%

## Time Complexity to Remove Node
# Traverse the tree log(n),
# Worst case, removing the root node,
# Easy to find the node.
# Find min -> logn TC
# Removing the min node. -> logn tC
# Total TC = O(2logn) = O(logn)
