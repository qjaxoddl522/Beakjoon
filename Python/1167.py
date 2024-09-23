import sys
input = sys.stdin.readline
from collections import deque

def bfs(root):
    #거리
    visited = [-1 for _ in range(V+1)]
    
    q = deque()
    q.append((root, 0))
    while q:
        node, dist = q.popleft()
        visited[node] = dist
        for nextNode, d in tree[node]:
            if visited[nextNode] == -1:
                q.append((nextNode, dist + d))
    maxDist = max(visited)
    return (visited.index(maxDist), maxDist)
                
V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    line = list(map(int, input().rstrip().split()))
    #트리(간선 노드, 거리)에 정보 추가
    for i in range(1, len(line)-1, 2):
        tree[line[0]].append((line[i], line[i+1]))

#가장 먼 노드에서 가장 먼 거리 구하기
print(bfs(bfs(1)[0])[1])
