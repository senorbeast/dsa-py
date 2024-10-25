## BFS for BST
# DFS or BFS can be applied to any tree

# Breadth First Search
# Traversing a tree layer by layer. Also called level order traversal
# Can't use recursion since we are switching sub trees.

# Since its doesn't follow matryoshka doll pattern, we can't use recursion for BFS

# To do it iteratively.
# We keep track of nodes in a layer in a queue.

# Pop node from queue, add the children of popped node into the queue (in order)
# Proceed till len(queue)>0
# For each layer, loop over the queue when all the elements of a layer are added to the queue.
# But since we will be mutating the queue, during the for loop, we need to get a snapshot of the queue info
# when we start the for loop
# So, we know when the particular layer has finished and popped.
# This snapshot can be obtained by cloning the queue in diff variable during creating a queue. (cloning) Or
# Just keeping the length of the queue, when starting the for loop. Since len(queue), will be the length
# calculated when starting the for loop for that layer. And this will not be mutated when queue is mutated.

#%%
from collections import deque
from trees import TreeNode


def bfsbst(root: TreeNode | None ): 
    queue = deque()

    if root:
        # Appending the actuall node, not just the value
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("Level:", level)

        # len(queue) acts as a snapshot of length of queue when the for loop starts.
        for _ in range(len(queue)):
            curr = queue.popleft()
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

#%%


#%%

# Although there are 2 loops, the TC is not O(n^2)

# Since we only move over all the elements once.  ## n
# Operations for each node: And for every element, we add, to the queue, pop from the queue, and print.  ## 3
## The Total TC: O(3n) = O(n) and not O(n^2) because of nested loops.
## TC: O(n)
