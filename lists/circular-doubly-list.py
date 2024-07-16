class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.last = None
        self.size = 0

    def insert_front(self, value):
        self.size += 1

        if self.last is None:
            self.last = Node(value)
            self.last.next = self.last
            self.last.prev = self.last
            return

        new_node = Node(value)
        new_node.next = self.last.next
        new_node.prev = self.last
        self.last.next.prev = new_node
        self.last.next = new_node

    def insert_at(self, index, value):
        if index > self.size:
            return "insert_at() error: Index out of bounds"

        if index == 0:
            self.insert_front(value)
            return

        if index == self.size:
            self.insert_back(value)
            return

        aux = self.last.next
        for i in range(index - 1):
            aux = aux.next

        new_node = Node(value)
        new_node.next = aux.next
        aux.next.prev = new_node
        aux.next = new_node
        new_node.prev = aux

        self.size += 1

    def insert_back(self, value):
        self.size += 1

        if self.last is None:
            self.last = Node(value)
            self.last.next = self.last
            return

        aux = self.last.next
        self.last.next = Node(value)
        self.last.next.prev = self.last
        self.last = self.last.next
        self.last.next = aux

    def delete_front(self):
        if self.last is None:
            return "delete_front() error: List is empty"

        if self.last.next is self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next

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

        current = self.last.next
        for i in range(index - 1):
            current = current.next

        current.next = current.next.next
        current.next.prev = current

        self.size -= 1

    def delete_back(self):
        if self.last is None:
            return "delete_back() error: List is empty"

        if self.last.next is self.last:
            self.last = None
        else:
            prev_to_last = self.last.prev
            prev_to_last.next = self.last.next
            self.last.next.prev = prev_to_last
            self.last = prev_to_last

        self.size -= 1

    def search(self, value):
        if self.last is None:
            return None

        current = self.last.next
        while True:
            if current.value == value:
                return current

            current = current.next
            if current == self.last.next:
                return None

    def get_size(self):
        return self.size

    def print(self):
        if self.last is None:
            print("print() error: List is empty")
            return

        aux = self.last.next
        while aux is not self.last:
            print(aux.value, end=' <-> ')
            aux = aux.next

        print(aux.value)


# Example
lista = CircularDoublyLinkedList()

print("List size:", lista.get_size())
print(lista.delete_back())  # Error

# Insert elements
lista.insert_front(2)
lista.print()
lista.insert_front(1)
lista.print()

lista.insert_back(5)
lista.print()

lista.insert_at(2, 3)
lista.print()
lista.insert_at(3, 4)
lista.print()
lista.insert_at(0, 0)
lista.print()
print(lista.insert_at(10, 6))  # Error

print("List size:", lista.get_size())

# Search elements
print("Searched node:", lista.search(3))
print("Searched node:", lista.search(7))

# Delete elements
lista.delete_at(3)
lista.print()

lista.delete_back()
lista.print()

lista.delete_front()
lista.print()

print("List size:", lista.get_size())

# Deletion error example
lista.delete_back()
lista.print()

lista.delete_front()
lista.print()

lista.delete_back()
lista.print()   # Error

print(lista.delete_back())  # Error

print("List size:", lista.get_size())
