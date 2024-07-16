class SegmentTree():
    def __init__(self, N):
        # 트리 만들기
        self.N = N
        self.treeSize = 1 << ((N-1).bit_length() + 1)
        self.tree = [0] * self.treeSize

    def print(self):
        print(self.tree)
    
    def query(self, a, b):
        def solve(L, R, node, nodeL, nodeR):
            if R < nodeL or L > nodeR:
                return 0
            if L <= nodeL and R >= nodeR:
                return self.tree[node]

            mid = (nodeL + nodeR) // 2
            return solve(L, R, node*2, nodeL, mid) + \
                   solve(L, R, node*2+1, mid+1, nodeR)
        if a > b:
            a, b = b, a
        return solve(a, b, 1, 0, self.treeSize//2-1)

    def update(self, idx, n):
        idx = (self.treeSize // 2) + idx
        self.tree[idx] = n
        while (idx > 1):
            idx //= 2
            self.tree[idx] = self.tree[idx * 2] + \
                             self.tree[idx * 2 + 1]

MOD = 1000000007

N = int(input())
inp = [int(input()) for _ in range(N)]
size = max(inp) + 1

# 거리를 나타내는 트리와 좌표에 존재하는 나무의 수를 나타내는 트리
distTree = SegmentTree(size)
countTree = SegmentTree(size)
ans = 1

distTree.update(inp[0], inp[0])
countTree.update(inp[0], 1)

for i in range(1, N):
    coor = inp[i]
    distTree.update(coor, distTree.query(coor, coor)+coor)
    countTree.update(coor, countTree.query(coor, coor)+1)

    # 새로운 나무를 심을 때마다 왼쪽에 있는 나무들과의 거리 합과
    # 오른쪽에 있는 나무들과의 거리 합을 구해 ans에 곱한다
    # 왼쪽 기준: 나무의 수 * 현재 좌표 - 왼쪽에 존재하는 모든 나무들의 좌표
    # = 왼쪽 나무들과의 거리 합이 된다
    leftSum = countTree.query(0, coor-1) * coor -\
              distTree.query(0, coor-1)
    rightSum = distTree.query(coor+1, size-1) -\
               countTree.query(coor+1, size-1) * coor
    ans = (ans * (leftSum + rightSum)) % MOD

print(ans)
