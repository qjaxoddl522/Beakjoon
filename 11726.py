n = int(input())
dp = [0]*(1001)
dp[1], dp[2] = 1, 2
for i in range(3, n+1):
    #제일 오른쪽을 가로 블록 2개로 채운 경우의 수 + 세로 블록 1개로 채운 경우의 수 = 피보나치 수열
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])
