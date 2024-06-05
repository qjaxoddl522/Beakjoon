import sys
input = sys.stdin.readline
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

#문명 번호의 루트를 찾는다
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def bfs():
    #문명이 합쳐진 횟수
    civil = 0
    while q:
        x, y, civilNum, year = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = civilNum
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nCivilNum = visited[nx][ny]
                if nCivilNum != 0:
                    if find(civilNum) == find(nCivilNum):
                        continue
                    #새로 방문한 칸이 다른 문명이면 union
                    root[root[nCivilNum]] = root[civilNum]
                    civil += 1
                    if civil == K-1:
                        return year
                else:
                    q.append((nx, ny, civilNum, year+1))

N, K = map(int, input().split())
#방문했을 경우 문명 번호 입력
visited = [[0]*N for i in range(N)]

#(x, y, 문명 번호, 연도)
q = deque()
for i in range(1, K+1):
    q.append((*map(lambda x : int(x)-1, input().split()), i, 0))

#각 문명의 루트 문명
root = [i for i in range(K+1)]
print(bfs())
