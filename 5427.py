from collections import deque
import sys
input = sys.stdin.readline

mx = (1, -1, 0, 0)
my = (0, 0, 1, -1)

def bfs():
    cnt = 0 #경과한 시간
    while q:
        cnt += 1
        while qFire and qFire[0][2] < cnt: #가장 앞불의 시간이 현재 시간보다 작을 경우에만(한번에 모두 번지는 것 방지)
            x, y, time = qFire.popleft()
            for i in range(4):
                nx = x + mx[i]
                ny = y + my[i]
                if nx>=0 and nx<w and ny>=0 and ny<h:
                    if mp[nx][ny] == '.' or mp[nx][ny] == '@':
                        qFire.append((nx, ny, time+1))
                        mp[nx][ny] = '*'
        while q and q[0][2] < cnt:
            x, y, time = q.popleft()
            for i in range(4):
                nx = x + mx[i]
                ny = y + my[i]
                if nx>=0 and nx<w and ny>=0 and ny<h:
                    if mp[nx][ny] == '.' and not visit[nx][ny]:
                        q.append((nx, ny, time+1))
                        visit[nx][ny] = True
                else: #맵 밖으로 나갈 가능성 -> 맵 끝부분이므로 탈출
                    return cnt
    return "IMPOSSIBLE"

for _ in range(int(input())):
    h, w = map(int, input().rstrip().split())

    q = deque()
    qFire = deque()
    
    mp = []
    visit = [[False] * h for _ in range(w)]
    for i in range(w):
        mp. append(list(input().rstrip()))
        for j in range(h):
            if mp[i][j] == '@':
                q.append((i, j, 0))
                visit[i][j] = True
            if mp[i][j] == '*':
                qFire.append((i, j, 0))

    print(bfs())
