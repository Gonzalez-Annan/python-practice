"""
Practice example: Stack
Category: Data Structures
Variant: 5
"""


class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.pop())

# Practice variant 5
