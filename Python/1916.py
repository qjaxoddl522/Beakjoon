import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N, M = int(input()), int(input())
graph = [[] for _ in range(N+1)]
dist = [float('inf') for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
start, end = map(int, input().split())

visited = [False] * (N+1)
dist[start] = 0
hq = [(0, start)]
while hq:
    _, node = heapq.heappop(hq)
    if visited[node]:
        continue
    visited[node] = True

    for nextNode, d in graph[node]:
        if not visited[nextNode]:
            dist[nextNode] = min(dist[nextNode], dist[node] + d)
            heapq.heappush(hq, (dist[nextNode], nextNode))
print(dist[end])