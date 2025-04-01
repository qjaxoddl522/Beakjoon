import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = 2500
    # dp[i] = 길이가 i*2일 때 괄호 문자열 경우의 수
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        for j in range(i):
            dp[i] = (dp[i] + dp[i-j-1] * dp[j]) % 1000000007

    for _ in range(int(input())):
        L = int(input())
        print(0 if L%2==1 else dp[L//2])

main()