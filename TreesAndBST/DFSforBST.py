## DFS for BST
# DFS or BFS can be applied to any tree

# Depth first search
# Traversing in ascending order, or Inorder traversal.

#         4
#      3    6
#     2    5   7

# o/p
# 2 3 4 5 6 7


# For each node.
# First recursively traverse the left sub tree till leaf nodes.
# From this we get the lowest vals.
## Then use the node
# Then recursively traverse the right sub tree.
# Then proceed to parent node.


#%%

from trees import TreeNode

# Traversal in order, for sorted trees 
# Smallest values in left sub tree

# Sorted Tree: 
#          4
#        3   6
#      2    5   7 
#

def inorder(root: TreeNode | None):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


# TC: Since we go through every node in tree,
# TC = O(n), same as sorted arr.

#%%
#
#
# We can sort, random val with BST in TC O(nlogn)
# Just inserting an ele 1 by 1 in O(logn) TC for each insertion.
# For n eles, it will take TC: O(nlogn)
# Then to traverse and print it, InOrder (DFS)
# O(logn)

# But O(logn + nlogn) = O(nlogn)
## Therefore sorting random numbers with BST takes O(nlogn), TC


#%%


def preorder(root: TreeNode | None):
    if not root:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)


#%%


def postorder(root: TreeNode | None):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)


#%%


def reverseOrder(root: TreeNode | None):
    if not root:
        return

    reverseOrder(root.right)
    print(root.val)
    reverseOrder(root.left)


#%%

from insertRemove import newTree


#%%
inorder(newTree)
#%%
reverseOrder(newTree)

# %%
preorder(newTree)

# %%
postorder(newTree)

# %%
newTree.print_tree()

# %%
