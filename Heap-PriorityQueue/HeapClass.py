## Pushing a value to Heap/Priority Queue

# Following the Structure property. We need to insert at the end.
# For the Order property. The added node must have less value/equal to the parent. (for min heap),
## OR we would need to swap parent node and new node recursively till Order property is followed. (to maintain order property)


#%%

# Heap class


class Heap:
    def __init__(self):
        self.heap = [0]

    ## TC: O(logn), since heap always is a balanced tree/nearly balanced tree.
    # And atmost we would need to swap till the height of the tree
    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1  # last index

        # Percolate up (to maintain order property)

        while self.heap[i] <= self.heap[i // 2]:
            # Swap till Order Property is followed, i.e. every parent has less value than its child. (min heap)
            # tmp = self.heap[i]
            # self.heap[i] = self.heap[i // 2]
            # self.heap[i // 2] = tmp
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    ##  Popping
    # We always pop the min value.
    # Popping the priority element, that the root ele (index 1)
    ## We can't just recursively/ loopingly swap lower value to percolate up, because it can violate the order

    ## Although not intivuity, but most efficent.
    # Instead, we replace the root, with the last element of the array. And percolate downwards the tree
    # Swapping to put the new root value to proper place. (To satify order property: Parents < Children value)

    # Percolating down (No. of operations = height of tree)
    # Since heap/priority queue follows the structure property, its always a balanced tree.
    # So, height is logn

    ## Helper function # Percolate down
    # O(logi)
    def __percolateDown(self, i: int) -> None:

        # Percolate Down (Only runs till we atleast the left child)
        while 2 * i < len(self.heap):
            # Do we also have a right child,
            # and if right child is smaller than left child
            # and current node is greater than current root.
            ## Swap right child and current root. (pointer)
            ## New current root pointer will be our right child (# Percolate down)

            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[i] > self.heap[2 * i + 1]
            ):
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1

            # Else if current root > left child
            ## Swap left child and current root
            ## New current root pointer will be our left child (# Percolate down)

            elif self.heap[i] > self.heap[2 * i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                ## Order property already satisfied, before reaching the leaf layer
                break  # Terminate while loop

    ## TC: O(logn)
    def pop(self) -> (int | None):

        # Empty heap (with dummy value)
        if len(self.heap) == 1:
            return None

        if len(self.heap) == 2:
            # NOT RECURSION: This pop function is array's pop function not our pop function, which is for heaps.
            # And 2nd element becomes the root
            return self.heap.pop()

        res = self.heap[1]  # root

        # Move last value to root
        self.heap[1] = self.heap.pop(-1)

        i = 1  # current root pointer

        ## Percolate Down
        self.__percolateDown(i)

        # return popped root.
        return res

    # Heapify
    # Description in Heapify.py

    ## TC: O(n)
    def heapify(self, arr) -> None:

        # Satisfy structure prop
        # Not using the 1st index. (So, bringing the first index at the end.)
        arr.append(arr[0])
        self.heap = arr

        # Pointer for last parent.
        # Last i = len(self.heap) - 1
        # parent of i = i//2
        ## Can't percolate down on leaf nodes anyway.
        ## No, need to percolate over half the elements in tree.
        curr = (len(self.heap) - 1) // 2

        # Percolate Down for each parent.
        # Two nested loops ? Damn boi
        ## But we don't percolate down on half the elements
        while curr > 0:
            i = curr  # Just for our function
            self.__percolateDown(i)
            curr -= 1
