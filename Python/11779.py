import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())

# 최단 경로의 이전 정점
prev = [-1] * (N+1)
dist = [float('inf')] * (N+1)
dist[s] = 0
visited = [False] * (N+1)
hq = [(0, s)]
while hq:
    _, node = heapq.heappop(hq)
    if visited[node]:
        continue
    visited[node] = True
    for nextNode, d in graph[node]:
        newDist = dist[node] + d
        if dist[nextNode] > newDist:
            prev[nextNode] = node
            dist[nextNode] = newDist
            heapq.heappush(hq, (newDist, nextNode))

print(dist[e])
path = []
node = e
while node != -1:
    path.append(node)
    node = prev[node]
print(len(path))
print(*reversed(path))