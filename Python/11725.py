import sys
input = sys.stdin.readline
from queue import deque

#BFS
def findParent(root):
    parent = {} #root를 기준으로 한 정점의 부모 목록
    
    visited = {}
    q = deque([(root)])
    while q:
        cur = q.popleft()
        visited[cur] = True

        if cur not in line: #다음 정점이 없으면 스킵
            continue
        for i in line[cur]:
            if i in visited: #방문한 정점은 스킵
                continue
            parent[i] = cur
            q.append(i)
    return parent

N = int(input())

line = {} #연결된 정점
for _ in range(N-1):
    i, j = map(int, input().rstrip().split())
    line[i] = line[i]+[j] if i in line else [j]
    line[j] = line[j]+[i] if j in line else [i]

par = findParent(1)
for i in range(2, N+1):
    print(par[i])
