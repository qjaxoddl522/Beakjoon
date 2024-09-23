import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, d = map(int,input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

def bfs(root):
    dist = [-1] * (n+1) #루트부터 정점까지의 거리
    dist[root] = 0
    q = deque([root])

    while q:
        node = q.popleft()
        for nextNode, distance in tree[node]:
            if dist[nextNode] == -1:
                q.append(nextNode)
                dist[nextNode] = dist[node] + distance

    md = max(dist) #최대 거리
    return [dist.index(md), md] #가장 먼 노드, 거리 반환

print(bfs(bfs(1)[0])[1]) #가장 먼 노드를 구한 후 그 노드에서 가장 먼 거리
