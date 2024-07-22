from queue import PriorityQueue
from math import sqrt


class Heuristics:
    @staticmethod
    def manhattan_distance(node_a, node_b):
        return abs(node_a.row - node_b.row) + abs(node_a.col - node_b.col)

    @staticmethod
    def euclidean_distance(node_a, node_b):
        return sqrt((node_a.row - node_b.row) ** 2 + (node_a.col - node_b.col) ** 2)

    @staticmethod
    def chebyshev_distance(node_a, node_b):
        return max(abs(node_a.row - node_b.row), abs(node_a.col - node_b.col))


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.heuristic_value = -1
        self.path = []

    def calculate_heuristic(self, other, heuristic):
        self.heuristic_value = heuristic(self, other)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.row == other.row and self.col == other.col

    def __lt__(self, other):
        if not isinstance(other, Node):
            return False
        return self.heuristic_value < other.heuristic_value

    def __gt__(self, other):
        if not isinstance(other, Node):
            return False
        return self.heuristic_value > other.heuristic_value


class World:
    def __init__(self, world) -> None:
        self.world = world
        self.rows = len(world)
        self.cols = len(world[0])

        self.movement_4 = [[-1, 0],  # Up
                           [0, -1],  # Left
                           [0, 1],   # Right
                           [1, 0]]   # Down

    def best_first_search(self, start_row, start_col, end_row, end_col, heuristic):
        pq = PriorityQueue()

        source = Node(start_row, start_col)
        target = Node(end_row, end_col)

        source.calculate_heuristic(target, heuristic)
        pq.put(source)

        while not pq.empty():
            current_node = pq.get()

            if current_node == target:
                return current_node.path

            for move in self.movement_4:
                new_row = current_node.row + move[0]
                new_col = current_node.col + move[1]

                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.world[new_row][new_col] != 'x':
                    new_node = Node(new_row, new_col)
                    new_node.path = current_node.path + [(new_row, new_col)]
                    new_node.calculate_heuristic(target, heuristic)
                    pq.put(new_node)


# Example
map = [['.', '.', 'x', '.'],
       ['x', '.', '.', 'x'],
       ['.', 'x', '.', '.'],
       ['.', 'x', 'x', '.']]

world = World(map)
path = world.best_first_search(0, 0, 3, 3, Heuristics.manhattan_distance)
print(path)
