from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
maze = [0]
for _ in range(1, N+1):
    maze.append([0]+list(map(int, list(input().rstrip()))))

result = [[0] * (M+1) for _ in range(N+1)]
result[1][1] = 1

q = deque()
visited = [[False] * (M+1) for _ in range(N+1)]

q.append([1, 1])
visited[1][1] = True

lx = [1, -1, 0, 0]
ly = [0, 0, 1, -1]
while q:
    loc = q.popleft() #현재 위치
    for i in range(4):
        x = loc[0]+lx[i]
        y = loc[1]+ly[i]
        if  x > 0 and x <= N and y > 0 and y <= M:
            if maze[x][y] == 1 and not visited[x][y]:
                q.append([x, y])
                result[x][y] = result[loc[0]][loc[1]]+1
                visited[x][y] = True

print(result[N][M])
