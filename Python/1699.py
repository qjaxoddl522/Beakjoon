N = int(input())
dp = [i for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 : #제곱수로 표현할 때 가장 항의 개수가 작은 j를 찾는다
            dp[i] = dp[i-j*j] + 1
print(dp[N])
