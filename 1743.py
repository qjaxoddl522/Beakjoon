import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기
N, M, K = map(int, input().split())

global size
size = 0
ans = 0

def dfs(road, x, y):
    global size
    if x < 0 or x > N or y < 0 or y > M: #범위초과
        return False
    if road[x][y] == 1: #쓰레기가 있으면
        size += 1
        road[x][y] = 0
        dfs(road, x+1, y)
        dfs(road, x-1, y)
        dfs(road, x, y+1)
        dfs(road, x, y-1)
        return True
    return False

road = [[0] * (M+1) for _ in range(N+1)]

for _ in range(K):
    x, y = map(int, input().split())
    road[x][y] = 1

for i in range(N+1):
    for j in range(M+1):
        if dfs(road, i, j): #False 안나오면
            ans = max(size, ans)
        size = 0

print(ans)
