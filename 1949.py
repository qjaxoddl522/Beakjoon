import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(node):
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            #일단 리프 노드까지 내려감
            dfs(child)
            #우수 마을 선정
            dp[node][1] += dp[child][0]
            #우수 마을 선정 안되면 선정된 경우와 안된 경우 중 큰거
            dp[node][0] += max(dp[child][0], dp[child][1])

N = int(input())
population = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

#dp[i][1] = i번째 마을이 우수 마을일 경우 최대 우수 마을 인구
dp = [[0, population[i]] for i in range(N+1)]
visited = [False] * (N+1)

dfs(1)
print(max(dp[1]))
