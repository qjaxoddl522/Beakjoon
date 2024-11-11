import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop
"""
데이터 추가로 인해 다익스트라 풀이 불가능
"""
def dijkstra(start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    visited = [False] * (N+1)
    # 거리, 남은 비용, 현재 노드
    hq = [(0, M, start)]
    while hq:
        distance, remain_cost, curnode = heappop(hq)
        if visited[curnode]:
            continue
        visited[curnode] = True
        for nextnode, nextc, nextd in graph[curnode]:
            # 방문, 남은 비용 확인
            if not visited[nextnode] and remain_cost >= nextc:
                dist[nextnode] = min(dist[nextnode], distance + nextd)
                heappush(hq, (dist[nextnode], remain_cost - nextc, nextnode))
    return dist

for _ in range(int(input())):
    # 공항 수, 지원 비용, 티켓 정보의 수
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    
    dist = dijkstra(1)
    print(dist[N] if dist[N] != float('inf') else "Poor KCM")