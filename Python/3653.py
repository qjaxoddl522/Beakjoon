import sys
input = lambda: sys.stdin.readline().rstrip()

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

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    tree = SegmentTree(n+m)
    for i in range(n):
        tree.update(i, 1)

    inp = list(map(int, input().split()))
    ans = []
    # dvd의 인덱스 번호
    dvdIdx = {n-i+1: i-1 for i in range(1, n+1)}
    
    for i in range(m):
        # 위에 있는 dvd 수만큼 정답에 추가
        ans.append(tree.query(dvdIdx[inp[i]]+1, n+m))
        # 기존 자리는 0으로, 가장 위쪽을 1로 업데이트
        tree.update(dvdIdx[inp[i]], 0)
        tree.update(n+i, 1)
        # dvd 위치 갱신
        dvdIdx[inp[i]] = n+i
        
    print(*ans)
