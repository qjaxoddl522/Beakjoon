import sys
input = sys.stdin.readline

n, m = map(int, input().split())
#리프 노드가 두개면 리프 1개
leaf = 1 if m == 2 else 0

last_leaf = 0 #마지막 리프노드
#마지막 리프 쓰기 전까지 0에서 계속 연결하다가
#리프 1개 남았을 때 가지 쭉 연결하기
for i in range(1, n):
    if m > leaf:
        print(0, i)
        leaf += 1
    else:
        print(last_leaf, i)
    last_leaf = i
