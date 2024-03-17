import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

global size
size = 0

def dfs(x, y):
    global size
    if x < 0 or x >= N or y < 0 or y >= N: #범위초과
        return False
    if mp[x][y] == 1:
        size += 1
        mp[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

N = int(input())
mp = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = [] #각 단지 집의 수

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            ans.append(size)
        size = 0
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
