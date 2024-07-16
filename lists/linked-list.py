class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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

    def insert_at(self, index, value):
        if index > self.size:
            return "insert_at() error : Index out of bounds"

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
        aux.next = new_node

        self.size += 1

    def insert_back(self, value):
        self.size += 1

        if self.tail is None:
            self.tail = Node(value)
            self.head = self.tail
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next

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
            print(current.value, end='->')
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
linkedlist = LinkedList()

print("List size:", linkedlist.get_size())
print(linkedlist.delete_back())  # Error

# Insert elements
linkedlist.insert_front(2)
linkedlist.print()
linkedlist.insert_front(1)
linkedlist.print()

linkedlist.insert_back(5)
linkedlist.print()

linkedlist.insert_at(2, 3)
linkedlist.print()
linkedlist.insert_at(3, 4)
linkedlist.print()
linkedlist.insert_at(0, 0)
linkedlist.print()
print(linkedlist.insert_at(10, 6))  # Error

print("List size:", linkedlist.get_size())

# Search elements
print("Searched node:", linkedlist.search(3))
print("Searched node:", linkedlist.search(7))

# Delete elements
linkedlist.delete_at(3)
linkedlist.print()

linkedlist.delete_back()
linkedlist.print()

linkedlist.delete_front()
linkedlist.print()

print("List size:", linkedlist.get_size())

# Reverse list
linkedlist.reverse()
linkedlist.print()

# Deletion error example
linkedlist.delete_back()
linkedlist.print()

linkedlist.delete_front()
linkedlist.print()

linkedlist.delete_back()
linkedlist.print()  # Error

print(linkedlist.delete_back())  # Error

print("List size:", linkedlist.get_size())
