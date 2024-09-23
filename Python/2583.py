import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

M, N, K = map(int, input().split())
mp = [(M) * [1] for _ in range(N)] #가로N 세로M
global size
size = 0
ans = []

def dfs(x, y):
    global size
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if mp[x][y] == 1:
        mp[x][y] = 0
        size += 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

for _ in range(K): #제외범위 0으로 색칠
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            mp[i][j] = 0

for i in range(N):
    for j in range(M):
        if mp[i][j] == 1:
            if dfs(i, j):
                ans.append(size)
                size = 0
ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))
