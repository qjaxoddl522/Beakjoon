N = int(input())
dp = [[0] * (10) for _ in range(N+1)] #dp[i][j] = 길이가 i이고 앞에 오는 숫자가 j인 계단수
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1): #길이
    for j in range(10): #뒤에서 두번째 자리
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
