class LevenshteinBottomUp:
    def lev(self, a, b):
        len_a = len(a) + 1
        len_b = len(b) + 1

        table = [[0] * len_b for _ in range(len_a)]
        ops = [[""] * len_b for _ in range(len_a)]

        for i in range(len_a):
            table[i][0] = i
            ops[i][0] = "Delete " * i
        for j in range(len_b):
            table[0][j] = j
            ops[0][j] = "Add " * j

        for i in range(1, len_a):
            for j in range(1, len_b):
                if a[i - 1] == b[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                    ops[i][j] = ops[i - 1][j - 1] + "Nothing, "
                else:
                    minimo = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                    table[i][j] = 1 + minimo

                    if minimo == table[i - 1][j]:
                        ops[i][j] = ops[i - 1][j] + "Delete " + a[i - 1] + ", "
                    elif minimo == table[i][j - 1]:
                        ops[i][j] = ops[i][j - 1] + "Add " + b[j - 1] + ", "
                    else:
                        ops[i][j] = ops[i - 1][j - 1] + "Replace " + a[i - 1] + " with " + b[j - 1] + ", "

        return table[len_a - 1][len_b - 1], ops[len_a - 1][len_b - 1]


levenshtein = LevenshteinBottomUp()
distance, operations = levenshtein.lev("Corazon", "Cascara")
print("Distance:", distance)
print("Operations:", operations)

distance, operations = levenshtein.lev("cobra", "cobrar")
print("Distance:", distance)
print("Operations:", operations)

distance, operations = levenshtein.lev("pizza", "pizarron")
print("Distance:", distance)
print("Operations:", operations)

distance, operations = levenshtein.lev("perro", "gato")
print("Distance:", distance)
print("Operations:", operations)
