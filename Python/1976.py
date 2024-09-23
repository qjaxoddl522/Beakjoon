import sys
input = sys.stdin.readline

def find(node):
    if root[node] != node:
        root[node] = find(root[node])
    return root[node]

def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)
    if node1 == node2:
        return
    root[node2] = node1

N = int(input())
M = int(input())

root = [i for i in range(N)]
for i in range(N):
    inp = list(map(int, input().rstrip().split()))
    for j in range(N):
        if inp[j] == 1:
            union(i, j)

root = [-1] + root
city = list(map(int, input().rstrip().split()))
result = all(root[x] == root[city[0]] for x in city)
print("YES" if result else "NO")
