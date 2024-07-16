import sys
input = lambda: sys.stdin.readline().rstrip()

# a, b 구간의 합 구하기
def tree_sum(a, b):
    def solve(L, R, node, nodeL, nodeR):
        if R < nodeL or nodeR < L:
            return 0
        if L <= nodeL and nodeR <= R:
            return tree[node]

        mid = (nodeL + nodeR) // 2
        return solve(L, R, node*2, nodeL, mid) + \
               solve(L, R, node*2+1, mid+1, nodeR)
    return solve(a-1, b-1, 1, 0, treeSize//2-1)

# idx를 n으로 갱신
def tree_update(idx, n):
    idx = (treeSize // 2) + idx - 1
    tree[idx] = n
    # 상위 노드 설정
    while (idx > 1):
        idx //= 2
        tree[idx] = tree[idx*2] + tree[idx*2+1]

N, Q = map(int, input().split())
leaf = list(map(int, input().split()))

# 트리 만들기
treeSize = 1 << ((N - 1).bit_length() + 1)
tree = [0] * treeSize
# 리프 노드 설정
for i in range(N):
    tree[(treeSize // 2) + i] = leaf[i]
# 상위 노드 설정
for i in range((treeSize // 2) - 1, 0, -1):
    # 부모 노드 = 자식 노드들의 합
    tree[i] = tree[2 * i] + tree[2 * i + 1]

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    # 구간합 구하기
    if x > y:
        print(tree_sum(y, x))
    else:
        print(tree_sum(x, y))
    # 변경
    tree_update(a, b)
