"""
Practice example: Linked List
Category: Data Structures
Variant: 5
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node

    def values(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result


if __name__ == "__main__":
    items = LinkedList()
    items.append(1)
    items.append(2)
    items.append(3)
    print(items.values())

# Practice variant 5
