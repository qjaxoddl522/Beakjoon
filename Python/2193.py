n = int(input())
dp = [0] * (n+1) #n자리수만큼 크기 지정
dp[1] = 1

for i in range(2, n+1): #개수가 피보나치 수열임
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
