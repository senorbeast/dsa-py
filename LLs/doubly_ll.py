#%%
class ListNode:
    def __init__(self, val):
        self.val: int = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None


# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()


# %%

newLL = LinkedList()
newLL.print()
print("____")
newLL.insertFront(1)
newLL.insertFront(2)
print(newLL.head.val, newLL.tail.val)
newLL.insertEnd(3)
newLL.insertEnd(2)
newLL.print()

# %%
print(newLL.head.val, newLL.tail.val)
newLL.removeEnd()
newLL.removeFront()
newLL.print()

# %%

print(newLL.head.val, newLL.tail.val)

# %%
print(newLL.head.next.val, newLL.tail.prev.val)

# %%
