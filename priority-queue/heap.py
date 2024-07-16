class HeapNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value


# Max-Heap
class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __parent(self, i):
        return i // 2

    def __left_child(self, i):
        return 2 * i

    def __right_child(self, i):
        return 2 * i + 1

    def _swap(self, i, j):
        self.heap[i - 1], self.heap[j - 1] = self.heap[j - 1], self.heap[i - 1]

    def heapify(self, i):
        left = self.__left_child(i)
        right = self.__right_child(i)
        largest = i

        if left <= self.size and self.heap[left - 1].key > self.heap[largest - 1].key:
            largest = left

        if right <= self.size and self.heap[right - 1].key > self.heap[largest - 1].key:
            largest = right

        if largest != i:
            self._swap(i, largest)
            self.heapify(largest)

    def build_heap(self, array):
        self.heap = array
        self.size = len(array)

        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

    def peek(self):
        if self.size <= 0:
            print("peek() error: Empty heap")
            return None

        return self.heap[0].key, self.heap[0].value

    def pop(self):
        if self.size <= 0:
            print("pop() error: Empty heap")
            return None

        max_node = self.heap[0]
        last_node = self.heap.pop()
        self.size -= 1

        if self.size > 0:
            self.heap[0] = last_node
            self.heapify(1)

        return max_node.key, max_node.value

    def increase_key(self, index, key):
        if index > self.size or index < 1:
            print("increase_key() error: Index out of bounds")
            return

        if key < self.heap[index - 1].key:
            print("increase_key() error")
            return

        self.heap[index - 1].key = key
        while index > 1 and self.heap[index - 1].key > self.heap[self.__parent(index) - 1].key:
            self._swap(index, self.__parent(index))
            index = self.__parent(index)

    def insert(self, key, value=None):
        node = HeapNode(key, value)
        self.heap.append(node)
        self.size += 1
        i = self.size

        self.increase_key(i, key)

    def get_size(self):
        return self.size

    def print(self):
        if self.size == 0:
            print("print() error: Empty heap")
        else:
            print("[", end="")
            for i in range(self.size - 1):
                print(f"({self.heap[i].key}, {self.heap[i].value})", end=", ")
            print(f"({self.heap[self.size - 1].key}, {self.heap[self.size - 1].value})]")


queue = Heap()

print("Size:", queue.get_size())
print("Max:", queue.peek())  # Error
print("Extracted element:", queue.pop())  # Error

elements = [HeapNode(4, 1), HeapNode(1, 2), HeapNode(3, 3), HeapNode(2, 4),
            HeapNode(16, 5), HeapNode(9, 6), HeapNode(10, 7), HeapNode(14, 8),
            HeapNode(8, 9), HeapNode(7, 10)]

queue.build_heap(elements)
print("Size:", queue.get_size())

print("Max:", queue.peek())
queue.print()

queue.increase_key(9, 15)
queue.print()

print("Extracted element: ", queue.pop())
queue.print()

print("Extracted element: ", queue.pop())
queue.print()

print("Max:", queue.peek())

queue.increase_key(5, 20)
queue.print()

print("Size:", queue.get_size())

queue.pop()
queue.pop()
queue.pop()
queue.pop()

queue.print()

queue.insert(4, 10)
queue.print()
