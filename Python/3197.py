import sys
input = sys.stdin.readline
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

#호수 밖 방지
def in_range(y, x):
    return 0 <= y < R and 0 <= x < C

def find(v):
    if v == root[v[0]][v[1]]:
        return v
    root[v[0]][v[1]] = find(root[v[0]][v[1]])
    return root[v[0]][v[1]]


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if r1 != r2:
        if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]]:
            root[r2[0]][r2[1]] = r1
        elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]]:
            root[r1[0]][r1[1]] = r2
        else:
            root[r2[0]][r2[1]] = r1
            rank[r1[0]][r1[1]] += 1

R, C = map(int, input().split())
swan = [] #각 백조의 초기 위치
lake = [list(input().rstrip()) for _ in range(R)]
rank = [[0] * C for i in range(R)] #유니온 연산
visited = [[False] * C for _ in range(R)]
root = [[(i, j) for j in range(C)] for i in range(R)]

for y in range(R):
    for x in range(C):
        if lake[y][x] == 'L':
            swan.append((y, x))
            lake[y][x] = '.'
        #두 백조 다 발견했으면 끝
        if len(swan) == 2:
            break

#처음 상태 설정
melt = deque()
for i in range(R):
    for j in range(C):
        #방문 안했고 물인 공간이면 bfs로
        #같은 공간에 있는 물이 같은 루트를 가리키도록 만든다
        if not visited[i][j] and lake[i][j] == '.':
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            while q:
                y, x = q.popleft()
                root[y][x] = (i, j)
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if in_range(ny, nx) and not visited[ny][nx] and lake[ny][nx] == '.':
                        #방문하지 않은 물이면 방문처리 후 다음 큐에 넣기
                        visited[ny][nx] = True
                        q.append((ny, nx))
                    if in_range(ny, nx) and not visited[ny][nx] and lake[ny][nx] == 'X':
                        #방문하지 않은 얼음이면 방문처리 후 녹이는 큐에 넣기
                        #이렇게 하면 가장자리 얼음만 녹는 큐에 들어감
                        visited[ny][nx] = True
                        melt.append((ny, nx))

ans = 0
#백조가 같은 물로 합쳐질 때까지 반복함
while find(swan[0]) != find(swan[1]):
    next_melt = deque()
    while melt:
        y, x = melt.popleft()
        lake[y][x] = '.'
        #다른 영역의 물 합칠 리스트
        union_point = []
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(ny, nx) and not visited[ny][nx] and lake[ny][nx] == 'X':
                #방문하지 않은 얼음이면 다음 날에 녹을 얼음 큐에 넣기
                visited[ny][nx] = 1
                next_melt.append((ny, nx))
            elif in_range(ny, nx) and lake[ny][nx] == '.':
                #만약 녹는 얼음 옆 물이면 합치는 리스트에 넣기
                union_point.append((ny, nx))

        for coor in union_point:
            union(coor, (y, x))

    melt = next_melt
    ans += 1
print(ans)
