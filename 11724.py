import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

#DFS가 끝날때마다 +1를 하면 연결 요소의 개수가 된다
def dfs(line, v, visit): #(연결된 노드 리스트, 현재 방문 노드, 방문 여부 리스트)
    visit[v] = True
    for i in line[v]:
        if not visit[i]:
            dfs(line, i, visit)

N, M = map(int, input().split())
line = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    line[u].append(v) #서로 연결된 노드 추가
    line[v].append(u)

ans = 0 #연결 요소의 개수
visit = [False for _ in range(N+1)] #방문 여부
for i in range(1, N+1):
    if not visit[i]:
        dfs(line, i, visit)
        ans += 1

print(ans)
