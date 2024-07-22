class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1] * N  

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a]) 
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1

def kruskal(n, edges):
    mst = []
    union_find = UnionFind(n)
    edges.sort(key=lambda x: x[2])  # Sort based on weight

    for u, v, weight in edges:
        if union_find.find(u) != union_find.find(v):
            mst.append((u, v, weight))
            union_find.union(u, v)
    
    return mst

# Example
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
n = 4  # Number of vertices
mst = kruskal(n, edges)
print("Kruskal's MST:", mst)
