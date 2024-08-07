import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

# dp[i][j] = 'a'가 i개, 'z'가 j개일 때 나오는 경우의 수
dp = [[0] * (M+1) for _ in range(N+1)]

# 테이블 채우기
for i in range(N+1):
    dp[i][0] = 1
for j in range(M+1):
    dp[0][j] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

"""
현재 위치에서 'a'를 선택할 수 있는 경우의 수를 확인하여
k가 그 수보다 작거나 같으면 'a'를 결과에 추가, 그렇지 않으면
'z'를 결과에 추가하고 k 값을 조절
"""
result = ''
# 조절용 변수
n, m, k = N, M, K
while n > 0 and m > 0:
    # k번째 안쪽이면 'a' 추가
    if k <= dp[n-1][m]:
        result += 'a'
        n -= 1
    # 이전 경우의 수가 k번째 초과면 'z' 추가
    else:
        result += 'z'
        k -= dp[n-1][m]
        m -= 1

# 남은 문자 추가
result += 'a' * n
result += 'z' * m

# k가 1 초과로 남으면 범위 초과
print(result if k <= 1 else -1)
