from queue import PriorityQueue
from math import sqrt


class Heuristics:
    @staticmethod
    def manhattan_distance(node_a, node_b):
        return abs(node_a.row - node_b.row) + abs(node_a.col - node_b.col)

    @staticmethod
    def euclidean_distance(node_a, node_b):
        return sqrt((node_a.row - node_b.row) ** 2 + (node_a.col - node_b.col) ** 2)


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


class NodeAStar(Node):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.distance = 0

    def __lt__(self, other):
        if not isinstance(other, NodeAStar):
            return False
        return self.heuristic_value + self.distance < other.heuristic_value + other.distance

    def __gt__(self, other):
        if not isinstance(other, NodeAStar):
            return False
        return self.heuristic_value + self.distance > other.heuristic_value + other.distance


class World:
    def __init__(self, world) -> None:
        self.world = world
        self.rows = len(world)
        self.cols = len(world[0])

        self.movement_4 = [[-1, 0],  # Up
                           [0, -1],  # Left
                           [0, 1],  # Right
                           [1, 0]]  # Down

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.world[row][col] != 'x'

    def a_star(self, srow, scol, trow, tcol, heuristic):
        start_node = NodeAStar(srow, scol)
        start_node.distance = 0
        target_node = Node(trow, tcol)

        pq = PriorityQueue()
        pq.put(start_node)

        while not pq.empty():
            current_node = pq.get()
            if current_node == target_node:
                return current_node.path + [(current_node.row, current_node.col)]

            for move in self.movement_4:
                new_row, new_col = current_node.row + move[0], current_node.col + move[1]

                if self.is_valid_move(new_row, new_col):
                    new_node = NodeAStar(new_row, new_col)
                    new_node.distance = current_node.distance + 1
                    new_node.calculate_heuristic(target_node, heuristic)
                    new_node.path = current_node.path + [(current_node.row, current_node.col)]
                    pq.put(new_node)

        return None


# Example
map = [['.', 'x', '.', '.'],
       ['.', '.', 'x', 'x'],
       ['x', '.', '.', '.'],
       ['.', '.', 'x', '.']]

world = World(map)

start_row, start_col = 0, 0
target_row, target_col = 3, 3
heuristic_function = Heuristics.manhattan_distance
path = world.a_star(start_row, start_col, target_row, target_col, heuristic_function)
print("Path found:", path)
