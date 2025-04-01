import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def main():
    N, M = map(int, input().split())
    TG, TB, X, B = map(int, input().split())

    board = [list(input()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    hq = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == '*':
                heapq.heappush(hq, (0, i, j))
    
    result = N * M
    while hq:
        time, r, c = heapq.heappop(hq)
        if time > TG:
            break
        if visited[r][c]:
            continue
        visited[r][c] = True
        result -= 1
        
        for mr, mc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r+mr, c+mc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == '#':
                    heapq.heappush(hq, (time+TB+1, nr, nc))
                else:
                    heapq.heappush(hq, (time+1, nr, nc))
    
    if result > 0:
        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    print(i+1, j+1)
    else:
        print(-1)

main()