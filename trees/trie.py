class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def char_to_idx(self, c):
        return ord(c) - ord('a')

    def insert(self, word):
        curr_node = self.root

        for c in word:
            idx = self.char_to_idx(c)
            if curr_node.children[idx] is None:
                curr_node.children[idx] = Node()

            curr_node = curr_node.children[idx]

        curr_node.is_leaf = True

    def search(self, word):
        curr_node = self.root

        for c in word:
            idx = self.char_to_idx(c)

            if curr_node.children[idx] is None:
                return False

            curr_node = curr_node.children[idx]

        return curr_node.is_leaf


# Example
trie = Trie()
trie.insert('algorithms')
trie.insert('algo')
trie.insert('hi')
print(trie.search('algorithms'))
print(trie.search('algo'))
print(trie.search('hello'))
