class NQueenSolver:
    def __init__(self, n):
        self.n = n

        self.rows = [0] * n
        self.LR = [0] * (2 * n)
        self.RL = [0] * (2 * n)

        self.solutions = [-1] * n
        self.nsolutions = 0

    def find_solutions(self):
        self.__find_solutions(0)

    def __find_solutions(self, curr_col):
        if curr_col == self.n:
            self.nsolutions += 1
            print(self.nsolutions, " -> ", self.solutions)
            return

        for i in range(self.n):
            if not self.__is_square_attacked(i, curr_col):
                self.__set_square_status(i, curr_col, 1)
                self.solutions[curr_col] = i
                self.__find_solutions(curr_col + 1)
                self.__set_square_status(i, curr_col, 0)
                self.solutions[curr_col] = -1

    def __set_square_status(self, row, col, status):
        self.rows[row] = status
        self.LR[row + col] = status
        self.RL[row - col + self.n] = status

    def __is_square_attacked(self, row, col):
        return self.rows[row] or self.LR[row + col] or self.RL[row - col + self.n]


# Example
s = NQueenSolver(8)
s.find_solutions()
