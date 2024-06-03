import sys
input = sys.stdin.readline
from queue import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def union(ax, ay, bx, by):
    ax, ay = findRoot(ax, ay)
    bx, by = findRoot(bx, by)
    if ax != bx or ay != by:
        board[bx][by] = [ax, ay]

def findRoot(x, y):
    if board[x][y] != [x, y]:
        board[x][y] = findRoot(board[x][y][0], board[x][y][1])
    return board[x][y]

N, K = map(int, input().split())
#board[x][y] = [루트x, 루트y] 
board = [[None for _ in range(N+1)] for _ in range(N+1)]

#(x, y, 루트x, 루트y, 햇수)
q = deque([])
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = [x, y]
    
    #문명 전파
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #맵 밖
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue
        
        #만약 처음부터 붙어있으면 같은 문명 취급
        if board[nx][ny] != None and findRoot(x, y) != findRoot(nx, ny):
            K -= 1
            union(x, y, nx, ny)
        q.append((nx, ny, x, y, 1))

ans = 0
#만약 모든 문명이 하나가 되면 반복문 종료
while (q and K > 1):
    x, y, root_x, root_y, year = q.popleft()
    ans = year

    #맵 밖
    if x < 1 or x > N or y < 1 or y > N:
        continue
    #이미 문명이 있으면 합친다
    if board[x][y] != None:
        #같은 문명이면 무시
        if findRoot(x, y) == findRoot(root_x, root_y):
            continue
        other_root_x, other_root_y = board[x][y]
        K -= 1
        union(other_root_x, other_root_y, root_x, root_y)
    #비어있는 지역이면 문명 전파
    else:
        board[x][y] = [root_x, root_y]
        
    #문명 전파
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        q.append((nx, ny, root_x, root_y, year + 1))

print(ans)
