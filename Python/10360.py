import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
INF = int(1e9)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
    
    # 음의 루프 찾기
    minusloop = []
    dist = [INF] * N
    dist[0] = 0
    for loop in range(N):
        for node in range(N):
            for nextnode, d in graph[node]:
                if dist[node] != INF and dist[nextnode] > dist[node] + d:
                    dist[nextnode] = dist[node] + d
                    if loop == N-1:
                        minusloop.append(nextnode)
    
    # 음의 루프가 시작점과 연결되어있는지 확인
    canGoPast = False
    visited = [False] * N
    q = deque(minusloop)
    while q:
        node = q.popleft()
        if node == 0:
            canGoPast = True
            break
        if visited[node]:
            continue
        visited[node] = True
        for nextnode, _ in graph[node]:
            if not visited[nextnode]:
                q.append(nextnode)
    
    print(f"Case #{tc}: {'possible' if canGoPast else 'not possible'}")