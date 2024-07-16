import sys
input = lambda: sys.stdin.readline().rstrip()

""" 세그먼트 트리로 풀면 시간초과남
def tree_max(L, R):
    # (구하고자 하는 구간 L, R, 현재 보고 있는 노드 번호
    # , 노드가 포함하는 구간 L, R)
    def solve(L, R, node, nodeL, nodeR):
        if R < nodeL or nodeR < L:
            return 0
        if L <= nodeL and nodeR <= R:
            return tree[node]

        mid = (nodeL + nodeR) // 2
        return max(solve(L, R, node*2, nodeL, mid), \
               solve(L, R, node*2+1, mid+1, nodeR))
    return solve(L, R, 1, 0, treeSize // 2 - 1)

# idx를 n으로 갱신
def tree_update(idx, n):
    idx = (treeSize // 2) + idx
    tree[idx] = n
    # 상위 노드 설정
    while (idx > 1):
        idx //= 2
        tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1])

N = int(input())
A = list(map(int, input().split()))

# 트리의 크기는 리프 노드를 담을 수 있는 이진수 * 2
treeSize = 1 << (N-1).bit_length() + 1
tree = [0] * treeSize

# 리프노드 업데이트 순서
indexed = [(value, idx) for idx, value in enumerate(A)]
updateOrder = sorted(indexed, key=lambda x: (x[0], -x[1]))

for v, idx in updateOrder:
    tree_update(idx, (tree_max(0, idx) + 1))

print(tree[1])"""

# 이분 탐색
def binarySearch(e):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

N = int(input())
A = list(map(int, input().split()))
LIS = [A[0]]

for i in range(N):
    # LIS의 마지막 값과 비교하여 더 큰 경우에만 삽입
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    #아닐 경우 이분탐색된 위치를 변경시킴
    else:
        LIS[binarySearch(A[i])] = A[i]

print(len(LIS))
