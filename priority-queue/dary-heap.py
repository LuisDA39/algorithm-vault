class HeapNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value


# Max heap
class DaryHeap:
    def __init__(self, D):
        self.heap = []
        self.size = 0
        self.D = D

    def parent(self, idx):
        return (idx - 2)//self.D + 1

    def first_child(self, idx):
        return 2 + self.D * (idx - 1)

    def last_child(self, idx):
        return 2 + self.D * (idx - 1) + self.D - 1

    def _swap(self, i, j):
        self.heap[i - 1], self.heap[j - 1] = self.heap[j - 1], self.heap[i - 1]

    def heapify(self, i):
        largest = i

        for k in range(i + 1, i + self.D + 1):
            if k <= self.size and self.heap[k - 1].key > self.heap[largest - 1].key:
                largest = k

        if largest != i:
            self._swap(i, largest)
            self.heapify(largest)

    def build_heap(self, arreglo):
        self.heap = arreglo
        self.size = len(arreglo)

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
            print("increase_key() error: Key is less")
            return

        self.heap[index - 1].key = key
        while index > 1 and self.heap[index - 1].key > self.heap[self.parent(index) - 1].key:
            self._swap(index, self.parent(index))
            index = self.parent(index)

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


queue = DaryHeap(3)  # 3 child HeapNodes

queue.print()  # Error
queue.pop()  # Error
queue.peek()  # Error

elements = [HeapNode(4, 1), HeapNode(1, 2),
            HeapNode(3, 3), HeapNode(2, 4),
            HeapNode(16, 5), HeapNode(9, 6),
            HeapNode(20, 4), HeapNode(5, 7),
            HeapNode(23, 1), HeapNode(3, 20),
            HeapNode(11, 3), HeapNode(0, 13)]

queue.build_heap(elements)
queue.print()

print("Max:", queue.peek())

print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
print("Extracted:", queue.pop())

queue.print()

print("Max:", queue.peek())

queue.insert(35, 1)
queue.insert(21, 0)
queue.insert(7, 4)
queue.insert(6, 0)

queue.print()

print("Extracted:", queue.pop())
print("Extracted:", queue.pop())

queue.print()

print("Size:", queue.get_size())

queue.increase_key(3, 14)
queue.print()

print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
print("Extracted:", queue.pop())
