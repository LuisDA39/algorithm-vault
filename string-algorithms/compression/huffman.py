class HeapNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value


class HuffmanNode(HeapNode):
    def __init__(self, key, value=None):
        super().__init__(key, value)

        # Children
        self.left_child = None
        self.right_child = None


class Heap:
    def __init__(self):
        self.heap = []

    def build_heap(self, elements):
        self.heap = elements
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left].key < self.heap[smallest].key:
            smallest = left
        if right < len(self.heap) and self.heap[right].key < self.heap[smallest].key:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def extract_min(self):
        min_node = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return min_node

    def peek(self):
        return self.heap[0]


class HuffmanCoding:
    def __init__(self):
        self.original_text = ""
        self.freq_table = {}
        self.heap = Heap()
        self.huffman_tree = None
        self.table_conversion = {}

    def set_original_text(self, text):
        self.original_text = text

    def calculate_frequency_table(self):
        for c in self.original_text:
            if c in self.freq_table:
                self.freq_table[c] += 1
            else:
                self.freq_table[c] = 1

    def create_huffman_tree(self):
        elements = []

        for letter, freq in self.freq_table.items():
            elements.append(HuffmanNode(freq, letter))

        self.heap.build_heap(elements)

        while len(self.heap.heap) > 1:
            node1 = self.heap.extract_min()
            node2 = self.heap.extract_min()

            merged = HuffmanNode(node1.key + node2.key)
            merged.left_child = node1
            merged.right_child = node2

            self.heap.heap.append(merged)
            self.heap.build_heap(self.heap.heap)

        self.huffman_tree = self.heap.peek()

    def calculate_table_conversion(self):
        self.table_conversion = {}
        self.__dfs(self.huffman_tree, "")

    def __dfs(self, curr_node, curr_code):
        if curr_node is None:
            return

        if curr_node.value is not None:
            self.table_conversion[curr_node.value] = curr_code

        self.__dfs(curr_node.left_child, curr_code + "0")
        self.__dfs(curr_node.right_child, curr_code + "1")

    def get_compressed_text(self):  # Returns bit sequence
        encoded_text = ""
        for character in self.original_text:
            encoded_text += self.table_conversion[character]
        return encoded_text

    def decompress_text(self, compressed_text):
        current_node = self.huffman_tree
        decompressed_text = ""

        for bit in compressed_text:
            if bit == '0':
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if current_node.left_child is None and current_node.right_child is None:
                decompressed_text += current_node.value
                current_node = self.huffman_tree

        return decompressed_text


# Example
huffman = HuffmanCoding()
huffman.set_original_text("Hello World!")
huffman.calculate_frequency_table()
huffman.create_huffman_tree()
huffman.calculate_table_conversion()
compressed_text = huffman.get_compressed_text()
print("Compressed text:", compressed_text)
decompressed_text = huffman.decompress_text(compressed_text)
print("Decompressed text:", decompressed_text)
