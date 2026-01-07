class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is empty")

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Deque is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage with data
deque = Deque()
deque.add_rear(10)
deque.add_front(5)
deque.add_rear(15)
print("Deque:", deque.items)
print("Size:", deque.size())
print("Remove from front:", deque.remove_front())
print("Deque after removing from front:", deque.items)
print("Remove from rear:", deque.remove_rear())
print("Deque after removing from rear:", deque.items)