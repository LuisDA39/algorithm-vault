class Node:
    def __init__(self, value, left_idx, right_idx):
        self.value = value
        self.left_idx = left_idx
        self.right_idx = right_idx

        self.left_node = None
        self.right_node = None


class segment_tree:
    def __init__(self, values):
        self.values = values
        self. root = None

    def build(self):
        self.root = Node(0, 0, len(self.values) - 1)
        self.__build(self.root)

    def __build(self, current_node):
        # Base case - leaf node
        if current_node.left_idx is current_node.right_idx:
            current_node.value = self.values[current_node.left_idx]
        else:
            # Find node mid-range
            range = (current_node.left_idx + current_node.right_idx) // 2

            # Create left and right nodes
            current_node.left_node = Node(0, current_node.left_idx, range)
            current_node.right_node = Node(0, range + 1, current_node.right_idx)

            # Build left and right subtree
            self.__build(current_node.left_node)
            self.__build(current_node.right_node)

            # Combine child values
            current_node.value = current_node.left_node.value + current_node.right_node.value

    def range_query(self, left, right):
        return self.__range_query(self.root, left, right)

    def __range_query(self, node, left, right):
        if left <= node.left_idx and right >= node.right_idx:
            return node.value
        elif left > node.right_idx or right < node.left_idx:
            return 0
        else:
            return (self.__range_query(node.left_node, left, right) +
                    self.__range_query(node.right_node, left, right))

    def update(self, index, value):
        return self.__update(self.root, index, value)

    def __update(self, node, index, value):
        if node.left_idx == node.right_idx:
            node.value = value
        else:
            if index > node.right_idx or index < node.left_idx:
                return
            else:
                self.__update(node.right_node, index, value)
                self.__update(node.left_node, index, value)
            node.value = node.left_node.value + node.right_node.value


sg_tree = segment_tree([1, 7, 3, 6, 8, 9, 12, 1, 0, 4, 2])
sg_tree.build()
print(sg_tree.range_query(0, 4))

sg_tree.update(0, 2)
print(sg_tree.range_query(0, 4))
