import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def dijkstra(start):
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0

    hq = [(0, start)]
    while hq:
        _, node = heappop(hq)
        if visited[node]:
            continue
        visited[node] = True

        for next, d in graph[node]:
            if dist[next] > dist[node] + d:
                dist[next] = dist[node] + d
                heappush(hq, (dist[next], next))
    return dist


# 도시 수, 도로 수, 사용 가능한 비행기 수, 출발 노드, 도착 노드
n, m, f, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    i, j, c = map(int, input().split())
    graph[i].append((j, c))
    graph[j].append((i, c))
airplane = []
for _ in range(f):
    i, j = map(int, input().split())
    airplane.append((i, j))

startDist = dijkstra(s)
endDist = dijkstra(t)

# 비행기를 사용하지 않는 경우
ans = startDist[t]
for start, end in airplane:
    ans = min(ans, startDist[start] + endDist[end])
print(ans)