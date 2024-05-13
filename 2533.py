import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(node):
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            #얼리어답터가 아닐 경우: 자식은 얼리어답터여야함
            dp[node][0] += dp[child][1]
            #얼리어답터일 경우: 자식이 어떤지 상관 없이 적은 경우로
            dp[node][1] += min(dp[child])

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

#dp[i][1] = i번째가 얼리어답터일때 총 얼리어답터 수
dp = [[0, 1] for _ in range(N+1)]
visited = [False] * (N+1)
dfs(1)

print(min(dp[1]))
