import sys
input = lambda: sys.stdin.readline().rstrip()

def tree_sum(a, b):
    def solve(L, R, node, nodeL, nodeR):
        if R < nodeL or L > nodeR:
            return 0
        if L <= nodeL and R >= nodeR:
            return tree[node]

        mid = (nodeL + nodeR) // 2
        return solve(L, R, node*2, nodeL, mid) + \
               solve(L, R, node*2+1, mid+1, nodeR)
    return solve(a-1, b-1, 1, 0, treeSize//2-1)

def tree_update(idx, n):
    idx = (treeSize // 2) + idx - 1
    tree[idx] = n
    while (idx > 1):
        idx //= 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

N, M = map(int, input().split())

treeSize = 1 << ((N-1).bit_length() + 1)
tree = [0] * treeSize

for _ in range(M):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        if a > b:
            print(tree_sum(b, a))
        else:
            print(tree_sum(a, b))
    elif cmd == 1:
        tree_update(a, b)
