import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main() -> None:
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    inner = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        inner[b] += 1

    result = [0 for _ in range(N+1)]
    hq = []
    for i in range(1, N+1):
        if inner[i] == 0:
            heappush(hq, i)
    
    result = []
    while hq:
        node = heappop(hq)
        result.append(node)
        for next in graph[node]:
            inner[next] -= 1
            if inner[next] == 0:
                heappush(hq, next)
    print(*result)

main()