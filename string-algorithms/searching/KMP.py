class KMPMatching:
    def __init__(self):
        self.text = ""
        self.alphabet_size = 130

    def set_text(self, text):
        self.text = text

    def calculate_prefix_table(self, pattern):
        patt_len = len(pattern)
        table = [0] * patt_len
        i, j = 0, 1

        while j < patt_len:
            if pattern[i] == pattern[j]:
                table[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    table[j] = 0
                    j += 1
                else:
                    i = table[i - 1]

        return table

    def search(self, pattern):
        prefix_table = self.calculate_prefix_table(pattern)
        matches = []
        shift = 0
        shared_substr = 0

        while shift < len(self.text) - len(pattern) + 1:
            while shared_substr < len(pattern) and self.text[shift + shared_substr] == pattern[shared_substr]:
                shared_substr += 1

            if shared_substr == len(pattern):
                matches.append(shift)

            if shared_substr == 0:
                shift += 1
            else:
                shift += shared_substr - prefix_table[shared_substr - 1]
                shared_substr = max(0, prefix_table[shared_substr - 1])

        return matches


kmp = KMPMatching()

kmp.set_text("""The Knuth-Morris-Pratt (KMP) algorithm is an efficient pattern searching algorithm used 
            in computer science to search for occurrences of a pattern within a text. It was developed by Donald Knuth, 
            Vaughan Pratt, and James H. Morris in 1977. The KMP algorithm is based on the construction of a prefix table 
            that allows for avoiding unnecessary comparisons during the search. It is widely used in text processing, 
            string analysis, and search engines, among other applications.""")
pattern = 'algorithm'

found_matches = kmp.search(pattern)
print("Matches found in positions:", found_matches)
