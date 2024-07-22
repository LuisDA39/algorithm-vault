class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_right(self, N):
        if N <= 0:
            return

        self.root = Node(N)
        current_node = self.root

        while N > 1:
            current_node.right = Node(N - 1)
            current_node = current_node.right
            N -= 1

    def insert_left(self, N):
        if N <= 0:
            return

        self.root = Node(N)
        current_node = self.root

        while N > 1:
            current_node.left = Node(N - 1)
            current_node = current_node.left
            N -= 1

    def insert_zigzag(self, N):
        if N <= 0:
            return

        self.root = Node(N)
        current_node = self.root
        direction = True

        while N > 1:
            if direction:
                current_node.right = Node(N - 1)
                current_node = current_node.right
                direction = False
            else:
                current_node.left = Node(N - 1)
                current_node = current_node.left
                direction = True

            N -= 1

    def insert_sorted(self, N, values):
        if N <= 0 or len(values) != N:
            return

        values.sort()
        self.root = self.__insert_sorted(values)

    def __insert_sorted(self, values):
        if not values:
            return None

        mid = len(values) // 2
        root = Node(values[mid])

        root.left = self.__insert_sorted(values[:mid])
        root.right = self.__insert_sorted(values[mid + 1:])

        return root

    def print_inorder(self):
        print("inorder:", end=' ')
        self.__inorder(self.root)
        print()

    def __inorder(self, current_node):
        if current_node.left:
            self.__inorder(current_node.left)

        print(current_node.value, end=' ')

        if current_node.right:
            self.__inorder(current_node.right)

    def print_preorder(self):
        print("preorder:", end=' ')
        self.__preorder(self.root)
        print()

    def __preorder(self, current_node):
        print(current_node.value, end=' ')

        if current_node.left:
            self.__preorder(current_node.left)

        if current_node.right:
            self.__preorder(current_node.right)

    def print_postorder(self):
        print("postorder:", end=' ')
        self.__postorder(self.root)
        print()

    def __postorder(self, current_node):
        if current_node.left:
            self.__postorder(current_node.left)

        if current_node.right:
            self.__postorder(current_node.right)

        print(current_node.value, end=' ')


# Example
bt = BinaryTree()

print("Right")
bt.insert_right(5)
bt.print_inorder()
bt.print_preorder()
bt.print_postorder()

print("\nLeft")
bt.insert_left(5)
bt.print_inorder()
bt.print_preorder()
bt.print_postorder()

print("\nZigZag")
bt.insert_zigzag(5)
bt.print_inorder()
bt.print_preorder()
bt.print_postorder()

print("\nSorted")
bt.insert_sorted(5, [3, 1, 5, 2, 4])
bt.print_inorder()
bt.print_preorder()
bt.print_postorder()
