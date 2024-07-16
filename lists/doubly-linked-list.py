class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_front(self, value):
        self.size += 1

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        aux = self.head
        self.head = Node(value)
        self.head.next = aux
        aux.prev = self.head

    def insert_at(self, index, value):
        if index > self.size:
            return "insert_at() error: Index out of bounds"

        if index == 0:
            self.insert_front(value)
            return

        if index == self.size:
            self.insert_back(value)
            return

        aux = self.head
        for i in range(index - 1):
            aux = aux.next

        new_node = Node(value)
        new_node.next = aux.next
        new_node.prev = aux
        aux.next.prev = new_node
        aux.next = new_node

        self.size += 1

    def insert_back(self, value):
        self.size += 1

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete_front(self):
        if self.head is None:
            return "delete_front() error: List is empty"

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.size -= 1

    def delete_at(self, index):
        if index >= self.size:
            return "delete_at() error: Index out of bounds"

        if index == 0:
            self.delete_front()
            return

        if index == self.size - 1:
            self.delete_back()
            return

        prev = self.head
        for i in range(index - 1):
            prev = prev.next

        prev.next = prev.next.next
        prev.next.next.prev = prev

        self.size -= 1

    def delete_back(self):
        if self.head is None:
            return "delete_back() error: List is empty"

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next.next:
                current = current.next

            current.next = None
            self.tail = current

        self.size -= 1

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def get_size(self):
        return self.size

    def print(self):
        if self.head is None:
            print("print() error: List is empty")
            return

        current = self.head
        while current.next:
            print(current.value, end=' <-> ')
            current = current.next

        print(current.value)

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# Example
d_list = DoublyLinkedList()

print("List size:", d_list.get_size())
print(d_list.delete_back())  # Error

# Insert elements
d_list.insert_front(2)
d_list.print()
d_list.insert_front(1)
d_list.print()

d_list.insert_back(5)
d_list.print()

d_list.insert_at(2, 3)
d_list.print()
d_list.insert_at(3, 4)
d_list.print()
d_list.insert_at(0, 0)
d_list.print()
print(d_list.insert_at(10, 6))  # Error

print("List size:", d_list.get_size())

# Search elements
print("Searched node:", d_list.search(3))
print("Searched node:", d_list.search(7))

# Delete elements
d_list.delete_at(3)
d_list.print()

d_list.delete_back()
d_list.print()

d_list.delete_front()
d_list.print()

print("List size:", d_list.get_size())

# Reverse list
d_list.reverse()
d_list.print()

# Deletion error example
d_list.delete_back()
d_list.print()

d_list.delete_front()
d_list.print()

d_list.delete_back()
d_list.print()   # Error

print(d_list.delete_back())  # Error

print("List size:", d_list.get_size())
