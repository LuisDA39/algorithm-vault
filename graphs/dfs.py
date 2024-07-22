from collections import defaultdict


class GraphMat:
    def __init__(self, n_vertex):
        self.n_vertex = n_vertex

        self.adj_matrix = [[0]*self.n_vertex for _ in range(self.n_vertex)]
        self.visited = [0] * n_vertex

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def dfs(self, start):
        self.__dfs(start)

    def __dfs(self, curr_vertex):
        print(curr_vertex, end=" ")
        self.visited[curr_vertex] = 1

        for i in range(self.n_vertex):
            if (self.adj_matrix[curr_vertex][i] == 1) and self.visited[i] == 0:
                self.__dfs(i)

    def print_adj_matrix(self):
        for _ in self.adj_matrix:
            print(_)


class GraphList:
    def __init__(self, n_vertex):
        self.n_vertex = n_vertex

        self.adj_list = defaultdict(list)
        self.visited = [0] * n_vertex

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def dfs(self, start):
        self.__dfs(start)

    def __dfs(self, curr_vertex):
        print(curr_vertex, end=" ")
        self.visited[curr_vertex] = 1

        for i in self.adj_list[curr_vertex]:
            if self.visited[i] == 0:
                self.__dfs(i)

    def print_adj_list(self):
        for _ in self.adj_list:
            print(_, end=' -> ')
            for p in self.adj_list[_]:
                print(p, end=" ")
            print()


graph = GraphMat(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.print_adj_matrix()

print()

graph.dfs(2)

print("\n")

list = GraphList(5)
list.add_edge(0, 1)
list.add_edge(0, 2)
list.add_edge(1, 2)
list.add_edge(1, 3)
list.add_edge(2, 4)

list.print_adj_list()

print()

list.dfs(2)
