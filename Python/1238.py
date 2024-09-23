import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def dijkstra(start):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    visited = [False] * (N+1)
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
    return dist

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

answer = 0
fromPartyDist = dijkstra(X)
for i in range(1, N+1):
    answer = max(answer, fromPartyDist[i] + dijkstra(i)[X])
print(answer)