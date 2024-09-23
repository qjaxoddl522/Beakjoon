import sys
input = sys.stdin.readline

K = int(input())
order = list(map(int, input().rstrip().split()))

ans = [[] for _ in range(K)]

#중위 순회
#(방문 순서, 깊이)
def dfs(order, depth):
    #완전 이진 트리에서는 중앙이 루트
    mid = (len(order) // 2)

    #깊이에 해당하는 노드 추가
    ans[depth].append(order[mid])

    #마지막 노드면 끝
    if len(order) == 1:
        return

    dfs(order[:mid], depth+1)
    dfs(order[mid+1:], depth+1)

dfs(order, 0)

for i in ans:
    print(' '.join(map(str, i)))
