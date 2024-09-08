import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
papers = list(map(int, input().split()))

needs = [False] + [True] * (N)
for p in papers:
    needs[p] = False

# dp[i] = i번 페이지까지 존재할 때 사용한 최소 잉크
dp = [0] * (N+1)
for i in range(1, N+1):
    if needs[i]:
        if needs[i-1]:
            dp[i] = dp[i-1]+2
        else:
            dp[i] = dp[i-1]+7
        
        if i >= 2 and needs[i-2]:
            dp[i] = min(dp[i], dp[i-2]+4)
        if i >= 3 and needs[i-3]:
            dp[i] = min(dp[i], dp[i-3]+6)
    else:
        dp[i] = dp[i-1]

print(dp[N])