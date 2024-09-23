import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def dijkstra(start, end):
    dist = [float('inf')] * (N+1)
    visited = [False] * (N+1)
    dist[start], visited[start] = 0, 0
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
    return dist[end]

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

# 두 경로 중 짧은 것
path = [[(1, v1), (v1, v2), (v2, N)], [(1, v2), (v2, v1), (v1, N)]]
result = [0, 0]
for i in range(2):
    for s, e in path[i]:
        result[i] += dijkstra(s, e)
print(min(result) if min(result) != float('inf') else -1)