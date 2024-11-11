import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def dijkstra(start):
    dist = [float('inf')] * (N+1)
    visited = [False] * (N+1)

    dist[start] = 0
    q = [(0, start)]
    while q:
        _, node = heappop(q)
        if visited[node]:
            continue
        visited[node] = True

        for nextNode, d in graph[node]:
            if not visited[nextNode]:
                dist[nextNode] = min(dist[nextNode], dist[node] + d)
                heappush(q, (dist[nextNode], nextNode))
    return dist

N, M, D, E = map(int, input().split())
height = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, n = map(int, input().split())
    if height[a] < height[b]:
        graph[a].append((b, n))
    if height[a] > height[b]:
        graph[b].append((a, n))

home_dist = dijkstra(1)
target_dist = dijkstra(N)

ans = float('-inf')
for mid in range(2, N):
    if home_dist[mid] != float('inf') and target_dist[mid] != float('inf'):
        ans = max(ans, E * height[mid] - D * (home_dist[mid] + target_dist[mid]))
print(ans if ans != float('-inf') else "Impossible")