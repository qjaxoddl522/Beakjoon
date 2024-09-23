n, k = map(int, input().split()) #동전의 종류, 목표 가치
unit = [] #동전 단위
for i in range(n):
    unit.append(int(input()))
#i번째 동전까지 사용하여 j원을 만드는데 필요한 동전의 개수
dp = [([1000000] * (k+1)) for _ in range(n+1)]
for i in range(n):
    dp[i][0] = 0 #초기값 설정
    for j in range(k+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        jj = j + unit[i]
        if jj <= k:
            dp[i][jj] = min(dp[i][jj], dp[i][j] + 1)

if dp[n-1][k] == 1000000:
    print(-1)
else:
    print(dp[n-1][k])
