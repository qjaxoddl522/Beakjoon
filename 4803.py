import sys
input = sys.stdin.readline
from queue import deque

def bfs(x):
    isTree = True
    q = deque([x])
    while q:
        n = q.popleft()
        if visited[n]: #이미 방문한 정점(싸이클)
            #바로 리턴하지 않는 이유는 연결된 정점들을 방문하지 않은 채로 끝내면 안되기 때문
            isTree = False
        visited[n] = True
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
    return isTree

c = 0
while True:
    c += 1
    
    n, m = map(int, input().rstrip().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)] #간선
    for _ in range(m):
        i, j = map(int, input().rstrip().split())
        graph[i].append(j)
        graph[j].append(i)

    treeCnt = 0 #트리 개수
    visited = [False] * (n+1)

    for i in range(1, n+1):
        if not visited[i] and bfs(i):
            treeCnt += 1

    if treeCnt == 0:
        print(f"Case {c}: No trees.")
    elif treeCnt == 1:
        print(f"Case {c}: There is one tree.")
    else:
        print(f"Case {c}: A forest of {treeCnt} trees.")
