n = int(input())
dp = [0]*(n+1)
for i in range(2, n+1): #n까지 반복
    dp[i] = dp[i-1]+1 #세가지 경우의 수 모두 계산
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])
