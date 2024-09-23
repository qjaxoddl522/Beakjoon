import sys
input = sys.stdin.readline

#루트 합치기
def union(a, b):
    a = findRoot(a)
    b = findRoot(b)
    if a == b:
        return
    root[b] = a

#루트 찾기
def findRoot(node):
    if root[node] == node:
        return node
    root[node] = findRoot(root[node])
    return root[node]

n, m = map(int, input().split())

#각 노드의 루트노드
root = [i for i in range(n+1)]

for _ in range(m):
    mode, i, j = map(int, input().split())
    if mode == 0 and i != j:
        union(i, j)
    elif mode == 1:
        print("YES" if findRoot(i) == findRoot(j) else "NO")
