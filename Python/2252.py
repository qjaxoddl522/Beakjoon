import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    inner = [0 for _ in range(N+1)]
    time = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        inner[b] += 1

    result = [0 for _ in range(N+1)]
    dq = deque()
    for i in range(1, N+1):
        if inner[i] == 0:
            dq.append(i)
    
    result = []
    for _ in range(N):
        node = dq.popleft()
        result.append(node)
        for next in graph[node]:
            inner[next] -= 1
            if inner[next] == 0:
                dq.append(next)
    print(*result)

main()