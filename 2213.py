import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e9))

def dfs(node):
    visited[node] = True
    picked[node][1].append(node+1)
    for child in tree[node]:
        if not visited[child]:
            # 리프 노드까지 하강
            dfs(child)

            # 현재 노드가 선택되지 않음
            if dp[child][0] < dp[child][1]:
                dp[node][0] += dp[child][1]
                picked[node][0].extend(picked[child][1])
            else:
                dp[node][0] += dp[child][0]
                picked[node][0].extend(picked[child][0])

            # 현재 노드가 선택됨
            dp[node][1] += dp[child][0]
            picked[node][1].extend(picked[child][0])

n = int(input())
weight = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

# dp[현재 노드][현재 노드가 선택되었는지] = 최대 독립집합의 크기
dp = [[0, weight[i]] for i in range(n)]
visited = [False] * n
# picked[현재 노드][현재 노드가 선택되었는지] = [선택된 노드 리스트]
picked = [[[], []] for _ in range(n)]

dfs(0)

mxIdx = int(dp[0][0] < dp[0][1])
print(dp[0][mxIdx])
print(*sorted(picked[0][mxIdx]))
