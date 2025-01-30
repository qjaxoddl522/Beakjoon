import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 1000000

def main():
    while True:
        inp = input()
        if inp == "":
            break
        
        N = len(inp)
        # dp[i][j] = i번째에서 50원이 j개 남은 경우
        dp = [[0]*(N//2+1) for _ in range(N)]
        dp[0][1] = 1 if inp[0] != ")" else 0
        for i in range(1, N):
            if inp[i] == "(":
                for j in range(N//2-abs(N//2-i-1)+1):
                    dp[i][j] = dp[i-1][j-1] if j > 0 else 0
            elif inp[i] == ")":
                for j in range(N//2-abs(N//2-i-1)+1):
                    dp[i][j] = dp[i-1][j+1] if j < N//2 else 0
            else:
                for j in range(N//2-abs(N//2-i-1)+1):
                    if j > 0:
                        dp[i][j] += dp[i-1][j-1]
                    if j < N//2:
                        dp[i][j] += dp[i-1][j+1]
                    dp[i][j] %= MOD
        print(dp[N-1][0])

main()