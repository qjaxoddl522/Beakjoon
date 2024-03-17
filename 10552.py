import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

N, M, P = map(int, input().rstrip().split()) #노인 수, 채널 수, 초기 채널 번호
mp = [0] * (M+1)
for _ in range(N):
    i, j = map(int, input().rstrip().split())
    if mp[j] == 0: #바꿀 채널이 없으면 갱신
        mp[j] = i
visited = [False] * (M+1)
global ans
ans = 0

def dfs(ch):
    global ans
    if visited[ch]:
        ans = -1
        return
    visited[ch] = True
    if mp[ch] != 0:
        ans += 1
        dfs(mp[ch])
    return

dfs(P)
print(ans)
