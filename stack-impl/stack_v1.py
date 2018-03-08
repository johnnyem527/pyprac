class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.size() != 0:
            return self.items[len(self.items)-1]
        else:
            return None

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push('good')
print(s.peek())
s.push('ok')
print(s.peek())
print(s.size())
s.pop()
print(s.peek())
print(s.size())
s.pop()
print(s.peek())
print(s.size())