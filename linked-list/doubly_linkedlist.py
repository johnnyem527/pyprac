class DoublyLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.prevnode = None
        self.nextnode = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b
c.nextnode = a
a.prevnode = c

print(b.prevnode.value)