import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e9))

def divide(inLeft, inRight, postLeft, postRight):
    if postLeft > postRight:
        return

    root = postorder[postRight]
    result.append(root)
    
    inoRootIdx = inorderIdxDict[root]
    leftTreeSize = inoRootIdx - inLeft
    divide(inLeft, inoRootIdx-1, postLeft, postLeft+leftTreeSize-1)
    divide(inoRootIdx+1, inRight, postLeft+leftTreeSize, postRight-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

result = []
# 인덱스 검색용 딕셔너리
inorderIdxDict = {v: i for i, v in enumerate(inorder)}

divide(0, n-1, 0, n-1)
print(*result)
"""
6
4 2 5 1 3 6
4 5 2 6 3 1

1 2 4 5 3 6
"""
