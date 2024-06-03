import sys
input = sys.stdin.readline

def dfs(node):
    global ans
    ans += 1
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

ans = 0
dfs(1)
#1번 컴퓨터는 제외
print(ans-1)
