import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for _ in range(int(input())):
    t, k = map(int, input().split())
    ans = "no"
    if t == 1:
        #연결된 정점이 한 개 초과(루트 또는 리프 노드가 아님)
        if len(tree[k]) > 1:
            ans = "yes"
    #모든 간선은 단절선
    elif t == 2:
        ans = "yes"
    print(ans)
