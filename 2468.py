import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

N = int(input())
mp = [list(map(int, input().rstrip().split())) for _ in range(N)]

def dfs(x, y, h):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if not visited[x][y] and mp[x][y] > h:
        visited[x][y] = True
        dfs(x+1, y, h)
        dfs(x-1, y, h)
        dfs(x, y+1, h)
        dfs(x, y-1, h)
        return True
    return False

area = 0 #현재 영역의 개수
ans = 1 #수면의 높이가 0일 경우 안전 영역은 1

for h in range(1, max(map(max, mp))):
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if dfs(x, y, h):
                area += 1
    ans = max(ans, area)
    area = 0

print(ans)
