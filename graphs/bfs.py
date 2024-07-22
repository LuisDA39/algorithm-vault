from collections import defaultdict
from queue import Queue


class GraphMat:
    def __init__(self, n_vertex):
        self.n_vertex = n_vertex
        self.adj_matrix = [[0] * self.n_vertex for _ in range(self.n_vertex)]
        self.visited = [0] * n_vertex

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def print_adj_matrix(self):
        for _ in self.adj_matrix:
            print(_)

    def bfs(self, s):
        q = Queue()
        q.put(s)
        self.visited[s] = 1

        while not q.empty():
            c = q.get()
            print(c, end=" ")

            for i in range(self.n_vertex):
                if self.adj_matrix[c][i] == 1 and self.visited[i] == 0:
                    q.put(i)
                    self.visited[i] = 1


class GraphList:
    def __init__(self, n_vertex):
        self.n_vertex = n_vertex
        self.adj_list = defaultdict(list)
        self.visited = [0] * n_vertex

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def print_adj_list(self):
        for _ in self.adj_list:
            print(_, end=' -> ')
            for p in self.adj_list[_]:
                print(p, end=" ")
            print()

    def bfs(self, s):
        q = Queue()
        q.put(s)
        self.visited[s] = 1

        while not q.empty():
            c = q.get()
            print(c, end=" ")

            for p in self.adj_list[c]:
                if self.visited[p] == 0:
                    q.put(p)
                    self.visited[p] = 1


graph = GraphMat(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.print_adj_matrix()

print()

graph.bfs(2)

print("\n")

list = GraphList(5)
list.add_edge(0, 1)
list.add_edge(0, 2)
list.add_edge(1, 2)
list.add_edge(1, 3)
list.add_edge(2, 4)

list.print_adj_list()

print()

list.bfs(2)
