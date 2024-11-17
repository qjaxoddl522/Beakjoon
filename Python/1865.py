import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

# 시작점 컴포넌트 안에 음의 사이클이 있는지 판별
def isCycle(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    for loop in range(N):
        for node in range(1, N+1):
            for nextnode, d in graph[node]:
                if dist[node] != INF and dist[nextnode] > dist[node] + d:
                    dist[nextnode] = dist[node] + d
                    visited[nextnode] = True
                    if loop == N-1:
                        return True
    return False

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))
    
    # 서로 다른 컴포넌트를 고려한 벨만 포드
    isMinusLoop = False
    visited = [False] * (N+1)
    for start in range(1, N+1):
        if visited[start]:
            continue
        visited[start] = True
        if isCycle(start):
            isMinusLoop = True
            break
    print("YES" if isMinusLoop else "NO")