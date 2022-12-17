## Advantage of BST over, Binary Search on sorted Arrays.
# 1. Insert/Remove takes O(logn), instead of O(n)
# For balanced BST.

# AVL Tree: For better balanced tree


#%%
from trees import TreeNode


def insert(root, val):

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


#%%

newTree = TreeNode(2)
insert(newTree, 5)
print(newTree)

# %%
