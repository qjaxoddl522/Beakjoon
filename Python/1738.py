import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
graph_rev = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, -C))
    graph_rev[B].append(A)

dist = [INF] * (N+1)
dist[1] = 0
prev = [-1] * (N+1)
minusCycle = set()

for loop in range(N):
    for i in range(1, N+1):
        for nextnode, nextd in graph[i]:
            if dist[i] != INF and dist[nextnode] > dist[i] + nextd:
                dist[nextnode] = dist[i] + nextd
                prev[nextnode] = i
                if loop == N-1:
                    minusCycle.add(i)


# 음수 사이클이 도착점에 도달 가능한지 판별
isCycle = False
visited = [False] * (N+1)
q = deque([N])
while q:
    node = q.popleft()
    if visited[node]:
        continue
    visited[node] = True
    if node in minusCycle:
        isCycle = True
        break
    for pnode in graph_rev[node]:
        q.append(pnode)

# 경로에 사이클이 껴있거나 도착점에 도달 불가능
if isCycle or dist[i] == INF:
    print(-1)
else:
    path = [N]
    while prev[path[-1]] != -1:
        path.append(prev[path[-1]])
    path.reverse()
    print(*path)