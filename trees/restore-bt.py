class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

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

    def restore(self, inorder, preorder):
        self.root = self.__restore(inorder, preorder)

    def __restore(self, inorder, preorder):
        if not inorder or not preorder:
            return None

        root_value = preorder.pop(0)
        root = Node(root_value)

        inorder_idx = inorder.index(root_value)

        root.left = self.__restore(inorder[:inorder_idx], preorder)
        root.right = self.__restore(inorder[inorder_idx + 1:], preorder)

        return root


rec_inorder = [4, 2, 5, 1, 3]
rec_preorder = [1, 2, 4, 5, 3]

tree = BinaryTree()
tree.restore(rec_inorder, rec_preorder)

print("Traversals:")
tree.print_inorder()
tree.print_preorder()
