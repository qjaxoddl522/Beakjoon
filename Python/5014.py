from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        l = q.popleft()
        if l == G:
            return visited[l]
        for i in (U, -D):
            nl = l + i
            if 0<nl<=F and visited[nl] == -1:
                visited[nl] = visited[l] + 1
                q.append(nl)
    return "use the stairs"

F, S, G, U, D = map(int, input().rstrip().split())

q = deque()
q.append(S)
visited = [-1] * (F+1)
visited[S] = 0

print(bfs())
