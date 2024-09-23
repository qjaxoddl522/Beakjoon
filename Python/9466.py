import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

def dfs(t):
    global teams 
    
    visited[t] = True
    teamPre.append(t)
    select = team[t] #현재 팀원이 원하는 팀원
    
    if visited[select]:
        if select in teamPre:
            teams += len(teamPre[teamPre.index(select):])
    else:
         dfs(select)

global teams

T = int(input())
for _ in range(T):
    n = int(input()) #학생 수
    team = [0] + list(map(int, input().rstrip().split()))

    visited = [False] * (n+1)
    teams = 0 #소속된 팀 멤버 수
    
    for i in range(1, n+1):
        if not visited[i]:
            teamPre = [] #현재 팀
            dfs(i)

    print(n - teams)
