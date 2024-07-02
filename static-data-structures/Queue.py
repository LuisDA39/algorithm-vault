class Queue:
    def __init__(self, N):
        self.N = N
        self.head = 0
        self.tail = 0
        self.queue = [0] * (N + 1)

    def enqueue(self, value):
        if (self.tail + 1 == self.N + 1 and self.head == 0) or (self.tail + 1 == self.head):
            return "enqueue() error: Queue is full"

        self.queue[self.tail] = value
        self.tail += 1
        if self.tail == self.N + 1:
            self.tail = 0

    def dequeue(self):
        if self.is_empty():
            return "dequeue() error: Queue is empty"

        value = self.queue[self.head]
        self.head += 1
        if self.head == self.N + 1:
            self.head = 0
        return value

    def is_empty(self):
        return self.head == self.tail

    def get_front(self):
        if self.is_empty():
            return "get_front() error: Queue is empty"
        return self.queue[self.head]


# Example
queue = Queue(5)

print("Is empty?", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.enqueue(6))  # Error

print("Is empty?", queue.is_empty())
print("Front:", queue.get_front())

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print("Front:", queue.get_front())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())  # Error

print("Is empty?", queue.is_empty())
