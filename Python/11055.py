import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    ls = list(map(int, input().split()))
    dp = [i for i in ls]
    for i in range(N):
        for j in range(i):
            if dp[i] > dp[j]:
                dp[i] = max(dp[i], dp[j] + ls[i])
    print(max(dp))

main()