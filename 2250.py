import sys
input = sys.stdin.readline
from queue import deque

N = int(input())
#tree[노드] =
#[왼쪽 자식 노드, 오른쪽 자식 노드, 부모 노드, 깊이]
tree = [[0, 0, 0, 0] for _ in range(N+1)]

for _ in range(N):
    node, left, right = map(int, input().rstrip().split())
    tree[node][0] = left
    tree[node][1] = right

    #부모 노드 설정
    for i in (left, right):
        if i != -1:
            tree[i][2] = node

#루트노드 찾기
root = 0
for i in range(1, N+1):
    if tree[i][2] == 0:
        root = i

depthMax = 0 #최대 깊이
#BFS
q = deque() #[현재 노드, 깊이]
q.append([root, 1])
while q:
    node, depth = q.popleft()
    tree[node][3] = depth
    if depth > depthMax:
        depthMax = depth
    for i in (0, 1):
        if tree[node][i] != -1:
            q.append([tree[node][i], depth+1])

#중위 순회
def inorder(node):
    global order
    if tree[node][0] != -1:
        inorder(tree[node][0])

    depth = tree[node][3]
    leftend[depth] = min(leftend[depth], order)
    rightend[depth] = max(rightend[depth], order)
    order += 1
    
    if tree[node][1] != -1:
        inorder(tree[node][1])

#행별로 양쪽 끝 노드 구하기
leftend = [N for _ in range(depthMax+1)]
rightend = [0 for _ in range(depthMax+1)]

#열 번호 지정
order = 1 #열 번호
inorder(root)

#정답 레벨(깊이)와 너비 구하기
depthAns, lengthAns = 0, -1
for i in range(1, depthMax+1):
    if rightend[i] - leftend[i] > lengthAns:
        depthAns = i
        lengthAns = rightend[i] - leftend[i]

print(depthAns, lengthAns + 1) #출력 길이는 양쪽 노드 포함
