import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 1000000007

# (구하고자 하는 구간 L, R, 현재 보고 있는 노드 번호
# , 노드가 포함하는 구간 L, R)
def tree_mult(L, R, node, nodeL, nodeR):
    if R < nodeL or nodeR < L:
        return 1
    if L <= nodeL and nodeR <= R:
        return tree[node]

    mid = (nodeL + nodeR) // 2
    return (tree_mult(L, R, node*2, nodeL, mid) * \
           tree_mult(L, R, node*2+1, mid+1, nodeR)) % \
           MOD

# idx를 n으로 갱신
def tree_update(idx, n):
    idx = (treeSize // 2) + idx - 1
    tree[idx] = n
    # 상위 노드 설정
    while (idx > 1):
        idx //= 2
        tree[idx] = (tree[idx*2] * tree[idx*2+1]) % MOD

N, M, K = map(int, input().split())
leaf = [int(input()) for _ in range(N)]

# 트리 만들기
treeSize = 1 << ((N - 1).bit_length() + 1)
tree = [1] * treeSize
# 리프 노드 설정
for i in range(N):
    tree[(treeSize // 2) + i] = leaf[i] % MOD
# 상위 노드 설정
for i in range((treeSize // 2) - 1, 0, -1):
    # 부모 노드 = 자식 노드들의 곱
    tree[i] = (tree[2 * i] * tree[2 * i + 1]) % MOD

for _ in range(M+K):
    cmd, a, b = map(int, input().split())

    # 변경
    if cmd == 1:
        tree_update(a, b)
    # 합산
    elif cmd == 2:
        print(tree_mult(a-1, b-1, 1, 0, treeSize//2-1))
