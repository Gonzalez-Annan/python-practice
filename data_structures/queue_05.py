"""
Practice example: Queue
Category: Data Structures
Variant: 5
"""


from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    print(queue.dequeue())

# Practice variant 5
