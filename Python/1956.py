import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

V, E = map(int, input().split())
# 플로이드 워셜
dist = [[INF] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c
for m in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            dist[s][e] = min(dist[s][e], dist[s][m] + dist[m][e])

# 자기 자신으로의 거리가 가장 작은 값이 정답
answer = INF
for i in range(1, V+1):
    answer = min(answer, dist[i][i])
print(answer if answer != INF else -1)