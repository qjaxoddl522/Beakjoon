import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = input(), input()
lenA, lenB = len(A), len(B)

# 첫 번째 문자열의 i번째 문자와
# 두 번째 문자열의 j번째 문자까지의 LCS길이
dp = [[0 for _ in range(lenB+1)]\
       for _ in range(lenA+1)]

# 테이블 채우기
for i in range(1, lenA+1):
    for j in range(1, lenB+1):
        # 같은 문자를 발견하면 LCS길이+1
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 역순으로 복원
lcsLength = dp[lenA][lenB]
lcsStr = []
x1, x2 = lenA, lenB
while x1 > 0 and x2 > 0:
    # 같은 문자면 LCS문자
    if A[x1-1] == B[x2-1]:
        lcsStr.append(A[x1-1])
        x1 -= 1
        x2 -= 1
    # LCS 문자 첫 번째가 더 앞쪽에 있으면 나올때까지 빼기
    elif dp[x1-1][x2] > dp[x1][x2-1]:
        x1 -= 1
    else:
        x2 -= 1
lcsStr.reverse()

print(lcsLength)
print(''.join(lcsStr))
