import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

n, m = int(input()), int(input())
# dist[i][j] = i에서 j로 가는 최소거리
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
for _ in range(m):
    s, e, d = map(int, input().split())
    dist[s][e] = min(dist[s][e], d)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dist[i][j] if dist[i][j] != INF else 0, end=' ')
    print()