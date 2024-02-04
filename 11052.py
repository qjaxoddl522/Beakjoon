N = int(input())
P = [0]+list(map(int, input().split())) #N개의 카드가 들어있는 카드팩의 가격 P[N]
dp = [0] * (N+1) #N개 팔아서 얻을 수 있는 최대 이익 dp[N]

for i in range(1, N+1): #dp[i] 구하기
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j]) #dp[2-1] + P[1]

print(dp[N])
