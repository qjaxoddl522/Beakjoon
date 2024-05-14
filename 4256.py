import sys
input = sys.stdin.readline

def divide(preorder, inorder):
    if len(preorder) == 0: #자식 없음
        return
    if len(preorder) == 1: #한 개 남았으면 후위순회에 담기
        result.extend(preorder)
        return
    
    root = preorder[0] #전위순회 첫번째가 루트 노드
    inorderIdx = inorder.index(root)

    #후위 순회 과정
    divide(preorder[1:inorderIdx+1], inorder[:inorderIdx])
    divide(preorder[inorderIdx+1:], inorder[inorderIdx+1:])
    result.append(root)

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(input().split())
    inorder = list(input().split())

    #3 6 5 4 8 7 1 2
    #5 6 8 4 3 1 2 7
    result = []
    divide(preorder, inorder)
    print(" ".join(map(str, result)))
