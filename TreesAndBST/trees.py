## Binary Trees

# Complex.
# Similar to LL, where each node has a value and 2 pointers.
# Its Node similar to Doubly Linked List Node, since they too have a value and 2 pointers.
# But here the pointers are, called left, and right. Instead of prev and next as in DLL

# There is relationship between nodes , parent node, child node, left child node, right child node,
# descendants, ancestors, siblings

# Leaf Nodes: Doesn't have any children
# Root Node: Top Node

# Kind of opposite of a real tree.

## No cycles
## All nodes are connected someway.


## Height

# Height of single node = 1
# Height of any node = Starts from that node, goes down to the lowest descendant

## Depth

# Depth of root node is 1 or 0, how use want to say.

# Depth -> No. of pointer/edge required to reach the root node
# OR
# Depth -> No. of nodes including itself to reach the root node.


## Node values closest to a particular x node are
# left most node of right sub tree of x node : Closest larger value than x node
# right most node of left sub tree of x node : Closest smaller value than x node


#%%


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def print(self):
        print()
    
    
#%%

# Example usage
def create_ordered_tree(n):
    def create_subtree(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(mid)
        node.left = create_subtree(start, mid - 1)
        node.right = create_subtree(mid + 1, end)
        return node
    
    return create_subtree(1, n)


# Example usage for creating a tree with 40 nodes
newTree = create_ordered_tree(10)


# %%
