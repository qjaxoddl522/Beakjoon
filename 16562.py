import sys
input = sys.stdin.readline

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2:
        return
    root[root1] = root2
    cost[root2] = min(cost[root1], cost[root2])

def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]

N, M, k = map(int, input().split())
cost = list(map(int, input().rstrip().split()))
root = [i for i in range(N)]
for _ in range(M):
    v, w = map(int, input().split())
    union(v-1, w-1)

ans = 0
for i in range(N):
    if root[i] == i:
        ans += cost[i]

print(ans if k >= ans else "Oh no")
