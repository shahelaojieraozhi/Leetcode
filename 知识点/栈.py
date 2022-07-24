class S():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


Stack1 = S()
print(Stack1.isEmpty())

Stack1.push(5)
Stack1.push('adh')
Stack1.push(4)

print(Stack1.pop())
print(Stack1.size())
