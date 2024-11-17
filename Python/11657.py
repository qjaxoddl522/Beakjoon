import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

dist = [INF] * (N+1)
dist[1] = 0
minusCycle = False
# N-1번 까지만 돌아도 최소 경로가 보장되지만, 마지막에 한 번 더 루프를 돌아 갱신되는 노드가 있으면 음의 루프이다.
for loop in range(N):
    for i in range(1, N+1):
        for nextnode, nextd in graph[i]:
            if dist[i] != INF and dist[nextnode] > dist[i] + nextd:
                dist[nextnode] = dist[i] + nextd
                # 마지막 루프이면 음수로 끝없이 갱신되는 루프
                if loop == N-1:
                    minusCycle = True
if minusCycle:
    print(-1)
else:
    for i in range(2, N+1):
        print(dist[i] if dist[i] != INF else -1)