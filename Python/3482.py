import sys
input = sys.stdin.readline
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def bfs(stx, sty):
    visited = [[False] * C for _ in range(R)]
    #가장 먼 좌표와 거리
    x, y, d = 0, 0, 0
    #시작x, 시작y, 시작점으로부터의 거리
    q = deque([(stx, sty, 0)])

    while q:
        x, y, d = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and board[nx][ny] == '.' and not visited[nx][ny]:
                q.append((nx, ny, d+1))
    return [x, y, d]

T = int(input())
for _ in range(T):
    C, R = map(int, input().split())

    stx, sty = -1, -1
    board = []
    for i in range(R):
        col = list(input().rstrip())
        for j in range(C):
            #시작 위치 지정
            if col[j] == '.' and stx == -1:
                stx, sty = i, j
        board.append(col)
    #가장 먼 좌표에서 가장 먼 거리 찾기
    pos = bfs(stx, sty)
    ans = bfs(pos[0], pos[1])[2]
    print(f"Maximum rope length is {ans}.")
