import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e9))

def dfs(node):
    # 리프 노드면 1 리턴
    if not tree[node]:
        return 1
    
    for i in tree[node]:
        # 단방향으로 만들기 위해 삭제
        tree[i].remove(node)
        subtreeNode[node] += dfs(i)
    return subtreeNode[node]

N, R, Q = map(int, input().split())
tree = [set() for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

# 노드의 서브 트리 노드 수
subtreeNode = [1 for _ in range(N+1)]

# DFS로 서브 트리 노드 수 파악하기
dfs(R)

for _ in range(Q):
    inp = int(input())
    print(subtreeNode[inp])
