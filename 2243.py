import sys
input = lambda: sys.stdin.readline().rstrip()

class SegmentTree():
    def __init__(self, leafList):
        # 트리 만들기
        self.N = len(leafList)
        self.size = 1 << ((self.N-1).bit_length()+1)
        self.tree = [0] * self.size
        # 리프 노드 설정
        for i in range(self.N):
            self.tree[(self.size//2)+i] = leafList[i]
        # 상위 노드 설정
        for i in range((self.size//2)-1, 0, -1):
            # 부모 노드 = 자식 노드들의 합
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def query(self, k):
        pos = 1
        # 리프 노드에 도달할 때까지 내려가기
        while pos < (self.size // 2):
            # 왼쪽 자식이 목표값보다 크거나 같으면 왼쪽 자식으로 이동
            if self.tree[pos * 2] >= k:
                pos = pos * 2
            # 아닐 경우 왼쪽 자식의 값을 빼면서 오른쪽 자식으로 이동
            else:
                k -= self.tree[pos * 2]
                pos = pos * 2 + 1
        # 리프 노드 기준의 위치를 반환 (k=리턴값 맛의 k번째 사탕)
        return pos - (self.size // 2)

    def update(self, idx, n):
        idx = (self.size // 2) + idx
        self.tree[idx] += n
        while (idx > 1):
            idx //= 2
            self.tree[idx] = self.tree[idx*2] + \
                             self.tree[idx*2+1]

n = int(input())
# 맛에 따른 트리 (값은 사탕의 개수)
leaf = [0] * 1000000
tree = SegmentTree(leaf)

for _ in range(n):
    cmd = list(map(int, input().split()))

    # 사탕 꺼내기
    if cmd[0] == 1:
        taste = tree.query(cmd[1])
        print(taste)
        tree.update(taste, -1)

    # 사탕 넣기
    if cmd[0] == 2:
        tree.update(cmd[1], cmd[2])
