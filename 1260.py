from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
line = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    line[i].append(j)
    line[j].append(i)

for i in range(len(line)):
    line[i].sort()

d = []
def dfs(k):
    visited[k] = True
    d.append(k)
    for i in line[k]:
        if not visited[i]:
            dfs(i)

b = []
def bfs(k):
    q = deque([k])
    visited[k] = True
    while q: #큐가 비어있을때까지
        k = q.popleft() #첫번째 값 꺼내기
        b.append(k)
        for i in line[k]:
            if not visited[i]:
                q.append(i) #다음 단계 탐색을 위한 큐 삽입
                visited[i] = True

visited = [False] * (N+1)
dfs(V)
visited = [False] * (N+1)
bfs(V)
print(' '.join(map(str, d)))
print(' '.join(map(str, b)))
