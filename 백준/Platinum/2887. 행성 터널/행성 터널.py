def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) 
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

x_sorted = sorted((point[0], i) for i, point in enumerate(points))
y_sorted = sorted((point[1], i) for i, point in enumerate(points))
z_sorted = sorted((point[2], i) for i, point in enumerate(points))

edges = []

for i in range(N - 1):
    a, idx_a = x_sorted[i]
    b, idx_b = x_sorted[i + 1]
    edges.append((abs(a - b), idx_a, idx_b))

for i in range(N - 1):
    a, idx_a = y_sorted[i]
    b, idx_b = y_sorted[i + 1]
    edges.append((abs(a - b), idx_a, idx_b))

for i in range(N - 1):
    a, idx_a = z_sorted[i]
    b, idx_b = z_sorted[i + 1]
    edges.append((abs(a - b), idx_a, idx_b))
edges.sort()
parent = [i for i in range(N)]
rank = [0] * N
s = 0
count = 0

for cost, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        s += cost
        count += 1
        if count == N - 1:
            break

print(s)
