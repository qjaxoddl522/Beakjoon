import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

n, k = map(int, input().split())
# graph[i][j] = i와 j가 연결되어 있는가
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = -1
    graph[b][a] = 1

for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if graph[s][m] == 1 and graph[m][e] == 1:
                graph[s][e] = 1
            if graph[s][m] == -1 and graph[m][e] == -1:
                graph[s][e] = -1

for _ in range(int(input())):
    a, b = map(int, input().split())
    if graph[a][b] == INF:
        print(0)
    else:
        print(graph[a][b])