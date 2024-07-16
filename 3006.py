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
    # 범위 바깥이면 0 리턴
    if a > b:
        return 0
    return solve(a-1, b-1, 1, 0, treeSize//2-1)

def tree_update(idx, n):
    idx = (treeSize // 2) + idx - 1
    tree[idx] = n
    while (idx > 1):
        idx //= 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

N = int(input())
ls = [0] + [int(input()) for _ in range(N)]

# 미리 위치 저장해서 시간 초과 방지
posMap = {}
for i in range(1, N+1):
    posMap[ls[i]] = i

# 트리 만들기
treeSize = 1 << ((N-1).bit_length() + 1)
tree = [0] * treeSize
for i in range(N):
    tree_update(i+1, 1)

ans = []
for i in range(1, (N//2)+1):
    pos = posMap[i]
    swaps = tree_sum(1, pos-1) # 정렬에 필요한 교환 횟수 계산
    ans.append(swaps)
    tree_update(pos, 0) # 처리가 끝난 인덱스는 0으로
    
    pos = posMap[N-i+1]
    swaps = tree_sum(pos+1, N)
    ans.append(swaps)
    tree_update(pos, 0)

# N이 홀수면 생략된 0 추가
if N%2 == 1:
    ans += [0]

for i in ans:
    print(i)
