from collections import deque
import sys
input = sys.stdin.readline

mx = [1, 2, 2, 1, -1, -2, -2, -1] #나이트의 이동
my = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + mx[i]
            ny = y + my[i]
            if 0<=nx<L and 0<=ny<L and board[nx][ny] == -1:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
                if E == (nx, ny):
                    return board[nx][ny]
    return 0

for _ in range(int(input())):
    L = int(input())
    board = [[-1] * L for _ in range(L)]
    S = tuple(map(int, input().rstrip().split()))
    E = tuple(map(int, input().rstrip().split()))

    q = deque()
    board[S[0]][S[1]] = 0
    q.append(S)

    print(bfs())
