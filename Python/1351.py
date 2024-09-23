import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())

#모든 데이터를 담을 필요가 없기 때문에 딕셔너리를 사용하여 메모리 초과 방지
dp = {0:1}

def dfs(i):
    if i in dp:
        return dp[i]
    
    iP, iQ = i//P, i//Q
    
    if iP not in dp:
        dp[iP] = dfs(iP)
    if iQ not in dp:
        dp[iQ] = dfs(iQ)
        
    return dp[iP] + dp[iQ]

print(dfs(N))        
