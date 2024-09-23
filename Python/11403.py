import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

N = int(input())
inMap = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [0] * N

def dfs(x):
    for i in range(N):
        if inMap[x][i] == 1 and visited[i] == 0: #방문한적 없는 이동가능 경로
            visited[i] = 1
            dfs(i)

for i in range(N): #줄을 돌며 깊이우선탐색
    dfs(i)
    print(' '.join(map(str, visited)))
    visited = [0] * N
