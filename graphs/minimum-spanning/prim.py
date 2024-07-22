import heapq

def prim(n, edges):
    mst = []
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    adj_list = [[] for _ in range(n)]

    for u, v, weight in edges:
        adj_list[u].append((weight, v))
        adj_list[v].append((weight, u))

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst.append((u, weight))
        
        for next_weight, v in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (next_weight, v))
    
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
mst = prim(n, edges)
print("Prim's MST:", mst)
