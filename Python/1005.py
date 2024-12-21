import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    inner = [0] * (N+1)
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        inner[y] += 1
    W = int(input())
    
    result = [0] * (N+1)
    dq = deque()
    for i in range(1, N+1):
        if inner[i] == 0:
            result[i] = time[i]
            dq.append(i)
    
    for _ in range(N):
        node = dq.popleft()
        for next in graph[node]:
            inner[next] -= 1
            result[next] = max(result[next], result[node] + time[next])
            if inner[next] == 0:
                dq.append(next)
    print(result[W])

for _ in range(int(input())):
    main()