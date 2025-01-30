import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    energy = [tuple(map(int, input().split())) for _ in range(N-1)]
    energyBig = int(input())

    # 매우 큰 점프 사용 여부
    dp = [[float('inf')]*2 for _ in range(N)]
    dp[0][0] = 0
    for i in range(N-1):
        dp[i+1] = [min(dp[i+1][0], dp[i][0]+energy[i][0]), min(dp[i+1][1], dp[i][1]+energy[i][0])]
        if i+2 < N:
            dp[i+2] = [min(dp[i+2][0], dp[i][0]+energy[i][1]), min(dp[i+2][1], dp[i][1]+energy[i][1])]
        if i+3 < N:
            dp[i+3][1] = min(dp[i+3][1], dp[i][0]+energyBig)
    print(min(dp[N-1]))

main()