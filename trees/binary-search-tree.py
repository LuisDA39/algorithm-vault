class Node:
    def __init__(self, key, parent_node):
        self.key = key
        self.parent_node = parent_node
        self.left_node = None
        self.right_node = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search_iterative(self, key):
        current_node = self.root

        while current_node:
            if key == current_node.key:
                return current_node
            elif key > current_node.key:
                current_node = current_node.right_node
            else:
                current_node = current_node.left_node

        return None

    def insert_iterative(self, key):
        if not self.root:
            self.root = Node(key, None)

        current_node = self.root

        while True:
            if key < current_node.key:
                if not current_node.left_node:
                    current_node.left_node = Node(key, current_node)
                    return
                else:
                    current_node = current_node.left_node
            elif key > current_node.key:
                if not current_node.right_node:
                    current_node.right_node = Node(key, current_node)
                    return
                else:
                    current_node = current_node.right_node
            else:
                return

    def inorder_iterative(self):
        stack = []
        array = []
        current_node = self.root

        while current_node or len(stack) > 0:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left_node
            else:
                current_node = stack.pop()
                array.append(current_node.key)
                current_node = current_node.right_node

        return array

    def min(self, value):
        node = self.search_iterative(value)

        if node is None:
            return None

        while node.left_node is not None:
            node = node.left_node

        return node

    def max(self, value):
        node = self.search_iterative(value)

        if node is None:
            return None

        while node.right_node is not None:
            node = node.right_node

        return node

    def find_successor(self, value):
        node = self.search_iterative(value)

        if node is None:
            return None

        if node.right_node is not None:
            return self.min(node.right_node.key)
        else:
            parent = node.parent_node
            while parent is not None and parent.right_node == node:
                node = parent
                parent = node.parent_node

            return parent

    def find_predecessor(self, value):
        node = self.search_iterative(value)

        if node is None:
            return None

        if node.left_node is not None:
            return self.max(node.left_node.key)
        else:
            parent = node.parent_node
            while parent is not None and parent.left_node == node:
                node = parent
                parent = node.parent_node

            return parent

    def delete(self, value):
        node = self.search_iterative(value)

        if node is None:
            return None

        if node.left_node is None or node.right_node is None:
            y = node
        else:
            y = self.find_successor(node.key)

        if y.left_node is not None:
            x = y.left_node
        else:
            x = y.right_node

        if x is not None:
            x.parent_node = y.parent_node

        if y.parent_node is None:
            self.root = x
        elif y == y.parent_node.left_node:
            y.parent_node.left_node = x
        else:
            y.parent_node.right_node = x

        if y != node:
            node.key = y.key

        return y


bst = BinarySearchTree()
bst.insert_iterative(6)
bst.insert_iterative(8)
bst.insert_iterative(9)
bst.insert_iterative(11)
bst.insert_iterative(1)
bst.insert_iterative(3)
bst.insert_iterative(7)
bst.insert_iterative(2)
bst.insert_iterative(10)
bst.insert_iterative(12)
bst.insert_iterative(1)

print(bst.inorder_iterative())

bst.delete(8)

print(bst.inorder_iterative())

print(bst.search_iterative(1))
print(bst.find_successor(7).key)
print(bst.find_predecessor(12).key)
