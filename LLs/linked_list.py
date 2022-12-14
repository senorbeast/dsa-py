# Managing Pointers/ References

#%%


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr:
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ")
            curr = curr.next
        print()


#%%
LL = LinkedList()
LL.insertEnd(2)
LL.insertEnd(5)
LL.insertEnd(1)
print("LL", LL.head.val, LL.tail.val)
LL.insertFront(4)
LL.insertFront(8)
LL.insertEnd(7)
LL.print()
print("LL", LL.head.val, LL.tail.val)

# %%
LL.remove(0)
LL.print()

# %%
LL.remove(4)
LL.print()

# %%

LL.remove(1)
LL.print()

# %%
