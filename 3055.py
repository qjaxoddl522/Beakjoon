from collections import deque
import sys
input = sys.stdin.readline

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if visit[x][y] == "WATER":
            flag = "WATER" #이번 큐의 위치가 물이면 물이란 것을 표시
        else:
            flag = visit[x][y] #아니면 고슴도치이므로 걸린 시간 표시
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if nx>=0 and nx<h and ny>=0 and ny<w:
                if visit[nx][ny] == -1:
                    if flag == "WATER":
                        if mp[nx][ny] == '.': #물, 빈칸
                            visit[nx][ny] = flag
                            q.append((nx, ny))
                    else:
                        if mp[nx][ny] == '.': #고슴도치, 빈칸
                            visit[nx][ny] = flag + 1
                            q.append((nx, ny))
                        elif mp[nx][ny] == 'D': #고슴도치, 도착점
                            return flag + 1
    return "KAKTUS"

h, w = map(int, input().split())
q = deque()
mp = []
visit = [[-1] * w for _ in range(h)] #-1:미방문) 양수:해당 칸까지 걸린 시간) W:물)
for i in range(h):
    mp.append(list(input().rstrip()))
    for j in range(w):
        if mp[i][j] == 'S':
            mp[i][j] = '.'
            visit[i][j] = 0
            start = (i, j)
        elif mp[i][j] == '*':
            visit[i][j] = "WATER"
            q.append((i, j))

q.append(start) #물이 먼저 퍼져야하므로 고슴도치 큐는 나중에 추가
print(bfs())
