import sys
input = sys.stdin.readline
from queue import deque

mx, my = (1, -1, 0, 0), (0, 0, 1, -1)

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                if board[nx][ny] == 0: #갈 수 없음
                    visited[nx][ny] = 0
                elif board[nx][ny] == 1: #갈 수 있음
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

#목표지점부터 탐색
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i, j)

#출력
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
