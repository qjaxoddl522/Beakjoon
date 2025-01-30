import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 1_000_000_000

def main():
    N = int(input())
    # i명끼리 선물을 주고받은 경우의 수
    dp = [0] * (1_000_000+1)
    # (x에게 선물을 준 사람과 x가 선물을 준 사람이 동일인인 경우)
    # + (x에게 선물을 준 사람과 x가 선물을 준 사람이 다른 경우)
    # = (n-1) * dp[n-2] + (n-1) * dp[n-1]
    dp[1], dp[2] = 0, 1
    for i in range(3, N+1):
        dp[i] = ((i-1) * (dp[i-1] + dp[i-2])) % MOD
    print(dp[N])

main()