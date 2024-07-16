import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(L, R):
    # (구하고자 하는 구간 L, R, 현재 노드 번호
    # , 노드가 포함하는 구간 L, R)
    def sMin(L, R, node, nodeL, nodeR):
        # 현재 구간 전체가 범위 바깥
        if R < nodeL or nodeR < L:
            return int(1e10)
        # 현재 구간이 구하려는 범위에 포함
        if L <= nodeL and nodeR <= R:
            return treeMin[node]
        mid = (nodeL + nodeR) // 2
        return min(sMin(L, R, node*2, nodeL, mid), \
                   sMin(L, R, node*2+1, mid+1, nodeR))
    def sMax(L, R, node, nodeL, nodeR):
        if R < nodeL or nodeR < L:
            return 0
        if L <= nodeL and nodeR <= R:
            return treeMax[node]
        mid = (nodeL + nodeR) // 2
        return max(sMax(L, R, node*2, nodeL, mid), \
                   sMax(L, R, node*2+1, mid+1, nodeR))
    return sMin(L, R, 1, 0, treeSize//2-1), \
           sMax(L, R, 1, 0, treeSize//2-1)

N, M = map(int, input().split())
leaf = [int(input()) for _ in range(N)]

# 트리의 크기는 리프 노드를 담을 수 있는 이진수 * 2
treeSize = 1 << (N-1).bit_length() + 1
treeMin = [int(1e10)] * treeSize
treeMax = [0] * treeSize

# 리프 노드
for i in range(N):
    treeMin[(treeSize // 2) + i] = leaf[i]
    treeMax[(treeSize // 2) + i] = leaf[i]

# 상위 노드
for i in range((treeSize // 2) - 1, 0, -1):
    treeMin[i] = min(treeMin[2 * i], treeMin[2 * i + 1])
    treeMax[i] = max(treeMax[2 * i], treeMax[2 * i + 1])

# 정답 출력
for _ in range(M):
    a, b = map(int, input().split())
    print(*solve(a-1, b-1))
