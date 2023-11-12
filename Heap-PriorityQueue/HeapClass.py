## MinHeap: A min-heap is a binary tree such that the data contained in each node 
# is less than (or equal to) the data in that node's children

## Pushing a value to Heap/Priority Queue or Min Heap

# Following the Structure property. We need to insert at the end.
# For the Order property. The added node must have more value/equal to the parent. (for min heap),
## OR we would need to swap parent node and new node recursively till Order property is followed. (to maintain order property)


#%%

# Heap class

# Min Heap
class Heap:
    def __init__(self):
        self.heap = [0]

    ## TC: O(logn), since heap always is a balanced tree/nearly balanced tree.
    # And atmost we would need to swap till the height of the tree
    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1  # last index

        # Percolate up (to maintain order property)

        while self.heap[i] < self.heap[i // 2]:
            # Swap till Order Property is followed (Keep swapping till parent > child)
            # i.e. every parent has less value than its child. (min heap)
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

    ## Helper function # Percolate down, to satisfy the order property
    # O(logn)            (n is total elements in the heap)
    # logn is the height of the tree, max operations would be the height of the tree.

    def __percolateDown(self, i: int) -> None:

        # Percolate Down (Only runs till, we atleast have the  left)  [left child is 2*i]

        # Comparing order doesn't matter, you can compare right child first or left, 
        # Just make sure before swapping the min of the 3 is the new parent.
        while 2 * i < len(self.heap):  # Only run till, we atleast have the  left. [More percolating maybe required]
            if (
                2 * i + 1 < len(self.heap) # Do we also have a right child? [right child is (2*i) +1],
                and self.heap[2 * i + 1] < self.heap[2 * i] # and if right child is smaller than left child
                and self.heap[i] > self.heap[2 * i + 1] # and current node is greater than the right child
            ):
                ## Swap right child and current root. (pointer) [Percolate down if current node is greater than the right child]
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                ## New current root pointer will be our right child (# Percolate down)
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
    # Bottom layer doesn't need to percolate down. Operations reqd:   0 * (n/2)

    # 2nd last layer, can percolate once at max. Operations reqd: 1 * (n/4)     
    # [ 1 level down (max) to percolate for n/4 elements]
    
    # Total Operations: 
    # n -> Total no. of elements
    # h -> height of tree 

    # 0 * (n/2) + 1 *(n/4) + 2 * (n/8) + 3 * (n/16) + .... + (h*1)
    # n/4 * (Summation k = 1 to h of (k/(2^(k-1))))

    # TC = O(n)  [Heapify, build min/max heap from array]

    # Sorting is done in O(n)
    # But if we want an array from the heap, 
    # Popping required O(logn) for each element
    # Therefore, sorting an array requires O(nlogn) with heapify and popping to array in order.

    def heapify(self, arr: list) -> None:

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
