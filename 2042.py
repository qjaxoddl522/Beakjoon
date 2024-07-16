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

# idx를 n으로 갱신
def tree_update(idx, n):
    idx = (treeSize // 2) + idx - 1
    tree[idx] = n
    # 상위 노드 설정
    while (idx > 1):
        idx //= 2
        tree[idx] = tree[idx*2] + tree[idx*2+1]

N, M, K = map(int, input().split())
leaf = [int(input()) for _ in range(N)] 

# 트리 만들기
treeSize = 1 << (N.bit_length() + 1)
tree = [0] * treeSize
# 리프 노드 설정
for i in range(N):
    tree[(treeSize // 2) + i] = leaf[i]
# 상위 노드 설정
for i in range((treeSize // 2) - 1, 0, -1):
    # 부모 노드 = 자식 노드들의 합
    tree[i] = tree[2 * i] + tree[2 * i + 1]

for _ in range(M+K):
    cmd, a, b = map(int, input().split())

    # 변경
    if cmd == 1:
        tree_update(a, b)
    # 합산
    elif cmd == 2:
        print(tree_sum(a-1, b-1, 1, 0, treeSize//2-1))
