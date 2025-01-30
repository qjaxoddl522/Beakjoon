import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    T = int(input())
    dp = [0] * (1000001)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, len(dp)):
        for j in range(1, 4):
            dp[i] = (dp[i] + dp[i-j]) % 1000000009
    for _ in range(T):
        print(dp[int(input())])

main()