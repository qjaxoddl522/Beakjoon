import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq
from collections import deque

def dijkstra(start):
    visited = [False] * N
    dist = [float('inf')] * N
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        curDist, node = heapq.heappop(hq)
        if visited[node]:
            continue
        visited[node] = True
        for nextnode, d in graph[node]:
            if not visited[nextnode] and curDist + d < dist[nextnode]:
                dist[nextnode] = curDist + d
                heapq.heappush(hq, (dist[nextnode], nextnode))
    return dist

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        s, e, d = map(int, input().split())
        graph[s].append((e, d))
        
    # 최단 거리 경로 구하기
    Sdist = dijkstra(S)
    path = [[] for _ in range(N)]
    visited = [False] * N
    q = deque([S])
    while q:
        curnode = q.popleft()
        if visited[curnode]:
            continue
        visited[curnode] = True
        for nextnode, d in graph[curnode]:
            if Sdist[curnode] + d == Sdist[nextnode]:
                path[nextnode].append((curnode, d))
                q.append(nextnode)
    
    # 최단 거리 경로 삭제하기
    visited = [False] * N
    q = deque([D])
    while q:
        curnode = q.popleft()
        if visited[curnode]:
            continue
        visited[curnode] = True
        for prevnode, d in path[curnode]:
            if (curnode, d) in graph[prevnode]:
                graph[prevnode].remove((curnode, d))
                q.append(prevnode)
    Fdist = dijkstra(S)
    print(Fdist[D] if Fdist[D] != float('inf') else -1)