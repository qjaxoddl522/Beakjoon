import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

def dfs(v):
    cycleMem = [v] #현재 사이클에 속한 노드
    visited[v] = True
    group[v] = len(cycle) #현재 노드의 그룹 번호. 각 노드가 어떤 사이클에 속하는지를 알아냄

    while True:
        if group[want[v]] == -1: #다음 노드의 그룹 번호가 설정되지 않았을 경우
            group[want[v]] = group[v]
        else:
            group[v] = group[want[v]]

        v = want[v] #다음 노드로 이동
        if not visited[v]: #최초방문이면 사이클 멤버에 추가
            visited[v] = True
            cycleMem.append(v)
        else: #이미 방문한 상태면 사이클 형성
            if v in cycleMem:
                cycleStart = cycleMem.index(v)
                cycle.append(len(cycleMem) - cycleStart)
                notCycle.append(cycleStart)
                return
            else:
                notCycle[group[v]] += len(cycleMem) #사이클에 포함되지 않은 노드들 추가
                return

n, k = map(int, input().split())
want = [0] + list(map(int, input().rstrip().split()))

visited = [False] * (n+1)
cycle = []
notCycle = []
group = [0] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

#최적해를 위한 dp
dp = [[0] * (n+1) for _ in range(len(cycle)+1)] #dp[사이클의 수][탑승가능 인원] = 최대 탑승가능 인원

for i in range(1, len(cycle)+1):
    w = cycle[i-1] #현재 사이클의 크기
    r = notCycle[i-1] #현재 사이클에 속하지 않은 노드의 수
    for j in range(1, n+1):
        if w <= j:
            dp[i][j] = w
            if w+r >= j:
                dp[i][j] = j
            if dp[i-1][j-w] >= 0:
                dp[i][j] = max(dp[i-1][j-w] + w, dp[i-1][j], dp[i][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j])

#결과
ans = 0
for i in range(1, n+1):
    if dp[len(cycle)][i] >= 0 and dp[len(cycle)][i] <= k: #만족하는 값들 중 가장 큰 값 찾기
        ans = max(ans, dp[len(cycle)][i])
print(ans)
