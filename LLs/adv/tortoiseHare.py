
#%% 

## Floyd's Tortoise and Hare Algorithm

## Fast and Slow pointers

# Uses:
#   To find mid point of LL, fast will reach the end. Slow will be mid-1
#   To test for cyclic LL, fast and slow will meet. 
#   (Eventually the fast pointer catches up with the slow pointer)




# now move the fast pointer twice and slow pointer once.
## Types 
# 1. slow pointer at first node, fast pointer at second node,
# 2. slow and fast pointer on same node 


## LL

## 1. For early mid
# 1 -> 2 -> 3 -> 4
# s    f  

## 2. For latter mid
# 1-> 2 -> 3 -> 4
# sf 

# %% 

## Find the mid of LL with two pointers

# TC: O(n)
# SC: O(1)

from ..linked_list import ListNode

def middleOfList(head: ListNode):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


#%%

## Determine if a linked list has a cycle
