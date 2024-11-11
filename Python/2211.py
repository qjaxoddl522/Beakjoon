import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 최단 경로의 이전 정점
prev = [-1] * (N+1)
dist = [float('inf')] * (N+1)
dist[1] = 0
visited = [False] * (N+1)
hq = [(0, 1)]
while hq:
    _, node = heapq.heappop(hq)
    if visited[node]:
        continue
    visited[node] = True
    for nextNode, d in graph[node]:
        if visited[nextNode]:
            continue
        newDist = dist[node] + d
        if dist[nextNode] > newDist:
            prev[nextNode] = node
            dist[nextNode] = newDist
            heapq.heappush(hq, (newDist, nextNode))
print(N-1)
for node in range(2, N+1):
    print(node, prev[node])