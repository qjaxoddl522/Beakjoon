import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().rstrip().split()))
    X_sum = [0]
    for i in range(N):
        X_sum.append(X_sum[i] + X[i])

    #최대 구간합 구하기
    ans = X[0] #초기값은 대충 존재 가능한 값으로
    for i in range(1, N+1): #구간합 길이
        for j in range(i, N+1): #도착점
            ans = max(ans, X_sum[j] - X_sum[j-i])
    print(ans)
