import sys
input = sys.stdin.readline

def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1] > rank[r2]:
        root[r2] = r1
    elif rank[r1] < rank[r2]:
        root[r1] = r2
    else: #랭크가 같으면 아무나
        root[r2] = r1
        rank[r1] += 1

def find(v):
    if v != root[v]:
        root[v] = find(root[v])
    return root[v]

n, m = map(int, input().split())
root = [i for i in range(n)]
rank = [0 for _ in range(n)]

for i in range(m):
    a, b = map(int, input().rstrip().split())
    #연결될 정점들이 루트가 같으면 사이클이다
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)
