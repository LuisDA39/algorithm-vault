# Implementation of the levenshtein distance using ONLY recursion
class LevenshteinRecursivo:
    def lev(self, a, b):
        if len(b) == 0:
            return len(a)

        if len(a) == 0:
            return len(b)

        if a[0] == b[0]:
            return self.lev(a[1:], b[1:])

        return 1 + min(self.lev(a[1:], b), self.lev(a, b[1:]), self.lev(a[1:], b[1:]))


# Implementation of the levenshtein distance using the top-down dynamic programming approach
class LevenshteinTopDown:
    def __init__(self):
        self.mem = {}

    def lev(self, a, b):
        len_a = len(a)
        len_b = len(b)

        if (len_a, len_b) in self.mem:
            return self.mem[(len_a, len_b)]

        if len_a == 0:
            self.mem[(len_a, len_b)] = len_b
        elif len_b == 0:
            self.mem[(len_a, len_b)] = len_a
        else:
            tail_a = a[1:]
            tail_b = b[1:]

            if a[0] == b[0]:
                self.mem[(len_a, len_b)] = self.lev(tail_a, tail_b)
            else:
                delete = self.lev(tail_a, b)
                insert = self.lev(a, tail_b)
                replace = self.lev(tail_a, tail_b)
                self.mem[(len_a, len_b)] = 1 + min(delete, insert, replace)

        return self.mem[(len_a, len_b)]


# Example
print("--- Recursive Levenshtein ---")
lev_recursive = LevenshteinRecursivo()
print("Distance:", lev_recursive.lev("cobra", "cobrar"))
print("Distance:", lev_recursive.lev("hablar", "entablar"))
print("Distance:", lev_recursive.lev("pizarron", "pizza"))
print("Distance:", lev_recursive.lev("perro", "gato"))
print("Distance:", lev_recursive.lev("corazon", "cascara"))

# With the simple recursive approach, this example takes a long time ...
# print("Distance:", lev_recursive.lev("electroencefalografista", "desoxirribonucleotido"))

print("--- Levenshtein using Top-Down ---")
lev_topdown = LevenshteinTopDown()
print("Distance:", lev_topdown.lev("cobra", "cobrar"))

lev_topdown = LevenshteinTopDown()
print("Distance:", lev_topdown.lev("hablar", "entablar"))

lev_topdown = LevenshteinTopDown()
print("Distance:", lev_topdown.lev("pizarron", "pizza"))

lev_topdown = LevenshteinTopDown()
print("Distance:", lev_topdown.lev("perro", "gato"))

lev_topdown = LevenshteinTopDown()
print("Distance:", lev_topdown.lev("corazon", "cascara"))

lev_topdown = LevenshteinTopDown()
print("Distance:", lev_topdown.lev("electroencefalografista", "desoxirribonucleotido"))
