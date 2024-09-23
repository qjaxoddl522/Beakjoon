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

    def query_min(self, a, b):
        if a > b:
            a, b = b, a
        L = (self.treeSize // 2) + a
        R = (self.treeSize // 2) + b
        result = self.N + 1
        while L <= R:
            if L % 2 == 1: # L이 오른쪽 자식일 때
                result = min(result, self.tree[L])
                L += 1
            if R % 2 == 0: # R이 왼쪽 자식일 때
                result = min(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result
    
    def query_max(self, a, b):
        if a > b:
            a, b = b, a
        L = (self.treeSize // 2) + a
        R = (self.treeSize // 2) + b
        result = 0
        while L <= R:
            if L % 2 == 1: # L이 오른쪽 자식일 때
                result = max(result, self.tree[L])
                L += 1
            if R % 2 == 0: # R이 왼쪽 자식일 때
                result = max(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result

    def update_min(self, idx, n):
        idx = (self.treeSize // 2) + idx
        self.tree[idx] = n
        while (idx > 1):
            idx //= 2
            self.tree[idx] = min(self.tree[idx * 2],\
                             self.tree[idx * 2 + 1])
    
    def update_max(self, idx, n):
        idx = (self.treeSize // 2) + idx
        self.tree[idx] = n
        while (idx > 1):
            idx //= 2
            self.tree[idx] = max(self.tree[idx * 2],\
                             self.tree[idx * 2 + 1])

for _ in range(int(input())):
    N, K = map(int, input().split())
    # 각 트리의 리프는 k번 DVD가 위치에 있는지를 나타냄
    minTree = SegmentTree(N)
    maxTree = SegmentTree(N)

    for i in range(N):
        minTree.update_min(i, i)
        maxTree.update_max(i, i)
    
    for _ in range(K):
        Q, A, B = map(int, input().split())
        
        if Q == 0:
            temp = minTree.query_min(A, A)
            minTree.update_min(A, minTree.query_min(B, B))
            minTree.update_min(B, temp)
            maxTree.update_max(A, maxTree.query_max(B, B))
            maxTree.update_max(B, temp)

        elif Q == 1:
            minLoc = minTree.query_min(A, B)
            maxLoc = maxTree.query_max(A, B)

            # 최소, 최대 위치안에 DVD가 존재해야함
            if minLoc == A and maxLoc == B:
                print("YES")
            else:
                print("NO")
