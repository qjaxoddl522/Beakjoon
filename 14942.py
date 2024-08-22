import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
energy = [int(input()) for _ in range(n)]
# (연결된 방, 거리)
connect = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    connect[a].append((b, c))
    connect[b].append((a, c))

MAX_J = (n+1).bit_length()
# room[i][j] = i번 방에서 j^2번 이동했을 때 (방 번호, 거리)
room = [[-1] * MAX_J for _ in range(n+1)]
visited = [False] * (n+1)
# bfs로 각 방의 부모를 지정
q = deque([1])
while q:
    i = q.popleft()
    visited[i] = True
    for ni, dist in connect[i]:
        if not visited[ni]:
            room[ni][0] = (i, dist)
            q.append(ni)

room[1][0] = (1, 10000) # 1번에 도착하면 움직이지 않음
for j in range(1, MAX_J):
    for i in range(1, n+1):
        r = room[room[i][j-1][0]][j-1][0]
        d = room[i][j-1][1] + room[room[i][j-1][0]][j-1][1]
        room[i][j] = (r, d)

result = []
for i, e in enumerate(energy):
    i = i+1 # 방 번호 넘버링 동기화
    for j in range(MAX_J-1, -1, -1):
        if room[i][j][1] <= e:
            e -= room[i][j][1]
            i = room[i][j][0]
    result.append(i)
print(*result, sep='\n')
