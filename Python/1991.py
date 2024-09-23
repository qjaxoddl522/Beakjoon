import sys
input = sys.stdin.readline

N = int(input())
route = {}
for _ in range(N):
    n, left, right = input().rstrip().split()
    route[n] = [left, right]

#전위 순회
def preorder(root):
    if root != '.': #(루트) (왼쪽 자식) (오른쪽 자식)
        print(root, end='') #상위 출력
        preorder(route[root][0]) #왼쪽부터
        preorder(route[root][1]) #오른쪽

#중위 순회
def inorder(root):
    if root != '.': #(왼쪽 자식) (루트) (오른쪽 자식)
        inorder(route[root][0])
        print(root, end='')
        inorder(route[root][1])

#후위 순회
def postorder(root):
    if root != '.': #(왼쪽 자식) (오른쪽 자식) (루트)
        postorder(route[root][0])
        postorder(route[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
