import sys
input = sys.stdin.readline
from collections import deque

n, m, K = map(int, input().rstrip().split())
jewel = [int(input()) for _ in range(K)] #보석이 있는 섬 번호
bridge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])

q = deque([]) #[현재 위치 정점 번호, 가지고 있는 보석 비트, 보석 개수]
#visited[정점][가지고 있는 보석 비트] = 가지고 있는 보석 개수
visited = [[-1] * (1 << K) for _ in range(n+1)]

def bfs():
    ans = 0
    q.append((1, 0, 0))
    visited[1][0] = 0

    while q:
        loc, jew, jew_num = q.popleft()

        #보석이 있는 정점이고 이미 주운 보석이 아닐 경우 줍기
        if loc in jewel and (jew & (1 << (jewel.index(loc)))) == 0:
            new_jew = jew | (1 << (jewel.index(loc)))
            visited[loc][new_jew] = jew_num + 1
            q.append((loc, new_jew, jew_num + 1))
            #print(str(loc)+'번 보석 줍기')
        
        #처음이 아닌 도착지점이면 값 갱신
        if loc == 1 and jew_num > 0:
            ans = jew_num
            continue

        #이동 가능한 정점으로 이동하기
        for i, intensity in bridge[loc]:
            #방문한 적 없고 견딜 수 있는 정점
            if visited[i][jew] == -1 and jew_num <= intensity:
                visited[i][jew] = jew_num
                q.append((i, jew, jew_num))
                #print(str(loc)+'에서 '+str(i)+'로 이동')
    return ans

print(bfs())
