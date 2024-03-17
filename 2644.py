from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().rstrip().split())
m = int(input())

relation = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)] #p1에 대한 촌수
for _ in range(m):
    i, j = map(int, input().rstrip().split())
    relation[i].append(j)
    relation[j].append(i)

q = deque()
visited = [False] * (n+1)

q.append(p1)
visited[p1] = True

while(q):
    p = q.popleft() #현재 선택된 사람
    for i in relation[p]:
        if not visited[i]:
            q.append(i)
            result[i] = result[p]+1 #이전 촌수 +1
            visited[i] = True

print(result[p2] if result[p2] != 0 else -1)
