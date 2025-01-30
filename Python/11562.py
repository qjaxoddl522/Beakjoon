import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

n, m = map(int, input().split())
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
for _ in range(m):
    u, v, b = map(int, input().split())
    dist[u][v] = 0
    if b == 1:
        dist[v][u] = 0
    else:
        dist[v][u] = 1

for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            dist[s][e] = min(dist[s][e], dist[s][m] + dist[m][e])

for i in range(int(input())):
    s, e = map(int, input().split())
    print(dist[s][e])