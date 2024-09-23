import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N, M = map(int, input().split())
wall = []
for _ in range(M):
    wall.append(list(map(int, list(input()))))
dist = [[float('inf')] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dist[0][0] = 0
hq = [(0, 0, 0)]
while hq:
    _, r, c = heapq.heappop(hq)
    if visited[r][c]:
        continue
    visited[r][c] = True

    for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r+mr, c+mc
        if 0<=nr<M and 0<=nc<N and not visited[nr][nc]:
            dist[nr][nc] = min(dist[nr][nc], dist[r][c] + wall[nr][nc])
            heapq.heappush(hq, (dist[nr][nc], nr, nc))
print(dist[M-1][N-1])