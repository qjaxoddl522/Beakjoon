from collections import deque
import sys
input = sys.stdin.readline

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0<=nx<w and 0<=ny<h:
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    for i in range(w):
        for j in range(h):
            if visited[i][j] == -1:
                return -1 #방문 못한 공간 있으면 -1
    return visited[x][y] #모두 방문했으면 가장 늦게 방문한 시간

h, w = map(int, input().rstrip().split())
board = []
q = deque()
visited = [[-1] * h for _ in range(w)]

for i in range(w):
    board.append(list(map(int, input().rstrip().split())))
    for j in range(h):
        if board[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 0
        elif board[i][j] == -1:
            visited[i][j] = -2 #벽

print(bfs())
