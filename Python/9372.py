import sys
input = sys.stdin.readline

def dfs(node, cnt):
    visited[node] = True
    for i in tree[node]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    visited = [True] + [False for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    print(dfs(1, 0))
    
