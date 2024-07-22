def knights_tour(n, heuristic):
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # Knight movements
    moves = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

    board[0][0] = 0

    if not solve(0, 0, 1, board, moves, heuristic):
        print("No solution")
    else:
        print_board(board)


def solve(row, col, index, board, moves, heuristic):
    if index == len(board) * len(board):
        return True

    for move in sorted(moves, key=lambda x: heuristic(row + x[0], col + x[1], board, moves)):
        new_row = row + move[0]
        new_col = col + move[1]

        if 0 <= new_row < len(board) and 0 <= new_col < len(board) and board[new_row][new_col] == -1:
            board[new_row][new_col] = index
            if solve(new_row, new_col, index + 1, board, moves, heuristic):
                return True

            board[new_row][new_col] = -1

    return False


def heur1(row, col, board, moves):
    count = 0
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < len(board) and 0 <= new_col < len(board) and board[new_row][new_col] == -1:
            count += 1
    return count


def heur2(row, col, board, moves):
    center = len(board) // 2
    distance_to_center = abs(center - row) + abs(center - col)
    count = 0
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < len(board) and 0 <= new_col < len(board) and board[new_row][new_col] == -1:
            count += 1
    return count * distance_to_center


def print_board(board):
    for row in board:
        print(row)


# Example
n = int(input("Board size: "))
print("Using heuristic 1:")
knights_tour(n, heur1)
print("\nUsing heuristic 2:")
knights_tour(n, heur2)
