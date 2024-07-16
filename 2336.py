import sys
input = lambda: sys.stdin.readline().rstrip()

class SegmentTree():
    def __init__(self, leafList):
        # 트리 만들기
        self.N = len(leafList)
        self.size = 1 << ((self.N-1).bit_length()+1)
        self.tree = [float('inf')] * self.size
        # 리프 노드 설정
        for i in range(self.N):
            self.tree[(self.size//2)+i] = leafList[i]
        # 상위 노드 설정
        for i in range((self.size//2)-1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])
    
    def query(self, a, b):
        # 트리에서 리프 노드 찾기
        L = (self.size // 2) + a
        R = (self.size // 2) + b
        result = self.N + 1
        while L <= R:
            # L이 오른쪽 자식이면 가지치기
            if L % 2 == 1:
                result = min(result, self.tree[L])
                L += 1
            # R이 왼쪽 자식이면 가지치기
            if R % 2 == 0:
                result = min(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result

    def update(self, idx, n):
        idx = (self.size // 2) + idx
        self.tree[idx] = n
        while (idx > 1):
            idx //= 2
            self.tree[idx] = min(self.tree[idx*2], \
                                 self.tree[idx*2+1])

N = int(input())
score = [[0, 0, 0] for _ in range(N)]

# 첫 번째 등수가 좋은 순으로 정렬 후, 두 번째 등수가 좋은 학생들 중
# 세 번째 등수 최솟값을 찾아 자신이 능가하는지 확인한다.
# 만약 두 번째 등수가 좋은 학생이 없거나 최솟값보다 좋으면 굉장한 학생
for i in range(3):
    student = list(map(int, input().split()))
    for j in range(N):
        score[student[j]-1][i] = j+1
score.sort(key=lambda x: x[0])

# 두 번째 등수가 리프 노드인 학생의 세 번째 등수
leaf = [float('inf')] * N
tree = SegmentTree(leaf)

wonderful_student = 0
# 첫 번째 등수가 좋은 학생부터 순회
for a, b, c in score:
    # 최솟값 확인
    if c < tree.query(0, b-1):
        wonderful_student += 1
    # 등수 업데이트
    tree.update(b-1, c)
print(wonderful_student)
