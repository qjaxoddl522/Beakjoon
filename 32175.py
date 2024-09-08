import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 10**9 + 7

N, H = map(int, input().split())
cups = list(map(int, input().split()))

# dp[i] = 컵을 높이 i로 쌓는 방법의 수
dp = [0] * (H+1)
dp[0] = 1

for i in range(1, H+1):
    for c in cups:
        if i-c >= 0:
            dp[i] = (dp[i] + dp[i-c]) % MOD

print(dp[H])