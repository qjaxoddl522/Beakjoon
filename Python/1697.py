from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        l = q.popleft()
        if l == K:
            return visited[l]
        for nl in (l+1, l-1, l*2):
            if 0<=nl<=mx and visited[nl] == -1:
                visited[nl] = visited[l] + 1
                q.append(nl)

N, K = map(int, input().rstrip().split())
mx = 100000

q = deque()
q.append(N)
visited = [-1] * (mx+1)
visited[N] = 0

print(bfs())
