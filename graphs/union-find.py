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


# Example (five elements)
uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print(uf.find(2))  
print(uf.parent)
