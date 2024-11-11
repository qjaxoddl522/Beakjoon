import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def dijkstra(start):
    # (i, k) => 정점 번호 i에서 남은 도로 포장 수 k일 때 사용한 최소 비용
    cost = [[float('inf')] * (K+1) for _ in range(N+1)]
    cost[start][K] = 0
    visited = [[False] * (K+1) for _ in range(N+1)]
    hq = [(0, start, K)]
    while hq:
        nowcost, node, k = heapq.heappop(hq)
        if visited[node][k]:
            continue
        visited[node][k] = True
        for nextnode, d in graph[node]:
            if not visited[nextnode][k]:
                if nowcost + d < cost[nextnode][k]:
                    cost[nextnode][k] = nowcost + d
                    heapq.heappush(hq, (cost[nextnode][k], nextnode, k))
                if k > 0 and nowcost < cost[nextnode][k-1]:
                    cost[nextnode][k-1] = min(cost[nextnode][k-1], cost[node][k])
                    heapq.heappush(hq, (cost[nextnode][k-1], nextnode, k-1))
    return cost

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

result = dijkstra(1)
print(min(result[N]))