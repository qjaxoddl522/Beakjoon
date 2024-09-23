import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def dijstra(node):
    if visited[node]:
        return
    visited[node] = True

    # 주변 노드 거리 갱신 + 거리 비용 우선순위큐에 삽입
    for nextNode, d in graph[node]:
        if not visited[nextNode]:
            dist[nextNode] = min(dist[nextNode], dist[node] + d)
            heapq.heappush(hq, (dist[nextNode], nextNode))

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
dist = [float('inf') for _ in range(V+1)]
visited = [False] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dist[K] = 0

hq = [(0, K)]
while hq:
    dijstra(heapq.heappop(hq)[1])

for i in dist[1:]:
    print(i if i != float('inf') else "INF")