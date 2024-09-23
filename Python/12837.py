import sys
input = lambda: sys.stdin.readline().rstrip()

# (구하고자 하는 구간 L, R, 현재 보고 있는 노드 번호
# , 노드가 포함하는 구간 L, R)
def tree_sum(L, R, node, nodeL, nodeR):
    if R < nodeL or nodeR < L:
        return 0
    if L <= nodeL and nodeR <= R:
        return tree[node]

    mid = (nodeL + nodeR) // 2
    return tree_sum(L, R, node*2, nodeL, mid) + \
           tree_sum(L, R, node*2+1, mid+1, nodeR)

# idx의 위치에 n추가
def tree_update(idx, n):
    idx = (treeSize // 2) + idx - 1
    tree[idx] += n
    # 상위 노드 갱신
    while (idx > 1):
        idx //= 2
        tree[idx] = tree[idx*2] + tree[idx*2+1]

N, Q = map(int, input().split())

# 트리 만들기
treeSize = 1 << ((N-1).bit_length() + 1)
tree = [0] * treeSize

for _ in range(Q):
    cmd, p, q = map(int, input().split())

    # 추가
    if cmd == 1:
        tree_update(p, q)
    elif cmd == 2:
        print(tree_sum(p-1, q-1, 1, 0, treeSize//2-1))
    
