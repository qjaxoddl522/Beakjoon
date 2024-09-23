import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def dijkstra(n):
    cost = [list(map(int, input().split())) for _ in range(n)]
    minCost = [[float('inf')] * n for _ in range(n)]
    minCost[0][0] = cost[0][0]
    visited = [[False] * n for _ in range(n)]

    # (비용, row, col)
    hq = [(0, 0, 0)]
    while hq:
        _, r, c = heapq.heappop(hq)
        if visited[r][c]:
            continue
        visited[r][c] = True

        for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r+mr, c+mc
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                minCost[nr][nc] = min(minCost[nr][nc], minCost[r][c] + cost[nr][nc])
                heapq.heappush(hq, (minCost[nr][nc], nr, nc))
    return minCost[n-1][n-1]

T = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Problem {T}: {dijkstra(n)}")
    T += 1