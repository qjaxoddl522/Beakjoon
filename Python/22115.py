import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    coffee = list(map(int, input().split()))

    # i카페인을 섭취했을 때 마신 최소 커피 수
    dp = [N+1] * (K+1)
    dp[0] = 0
    for c in coffee:
        for i in range(K, c-1, -1):
            dp[i] = min(dp[i], dp[i-c]+1)
    print(dp[K] if dp[K] != N+1 else -1)

main()