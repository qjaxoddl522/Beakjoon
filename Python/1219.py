import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
INF = float('inf')

N, A, B, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    S, E ,C = map(int, input().split())
    graph[S].append([E, -C])
earn = list(map(int, input().split()))

money = [-INF] * N
money[A] = earn[A]
gee = []
for loop in range(N):
    for node in range(N):
        for nextnode, c in graph[node]:
            if money != -INF and money[nextnode] < money[node] + c + earn[nextnode]:
                money[nextnode] = money[node] + c + earn[nextnode]
                if loop == N-1:
                    gee.append(nextnode)

isGee = False
visited = [False] * N
q = deque(gee)
while q:
    node = q.popleft()
    if node == B:
        isGee = True
        break
    if visited[node]:
        continue
    visited[node] = True
    for nextnode, _ in graph[node]:
        if not visited[nextnode]:
            q.append(nextnode)

if money[B] == -INF:
    print("gg")
elif isGee:
    print("Gee")
else:
    print(money[B])