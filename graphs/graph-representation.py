from collections import defaultdict


class GraphMat:
    def __init__(self, n_vertex):
        self.n_vertex = n_vertex

        self.adj_matrix = [[0]*self.n_vertex for _ in range(self.n_vertex)]

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def print_adj_matrix(self):
        for _ in self.adj_matrix:
            print(_)


class GraphList:
    def __init__(self, n_vertex):
        self.n_vertex = n_vertex

        self.adj_list = defaultdict(list)

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def print_adj_list(self):
        for _ in self.adj_list:
            print(_, end=' -> ')
            for p in self.adj_list[_]:
                print(p, end=" ")
            print()


graph = GraphMat(5)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 4)
graph.add_edge(1, 4)
graph.print_adj_matrix()

print()

list = GraphList(5)
list.add_edge(1, 3)
list.add_edge(2, 4)
list.add_edge(2, 1)
list.add_edge(3, 4)
list.add_edge(1, 4)

list.print_adj_list()
