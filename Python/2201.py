import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
# dp[i] = 길이가 i일 때 이친수의 개수
dp = [0, 1]

n = 1 # 이친수의 합
i = 2 # K는 i자리 이친수
# dp[i] = dp[i-2] + dp[i-1] => 피보나치 수열
while n < K:
    dp.append(dp[i-2] + dp[i-1])
    n += dp[-1]
    i += 1
# 길이가 i인 num번째 수가 정답
i -= 1
num = K - (n - dp[-1]) - 1
# print(f"길이가 {i}인 {num}번째 이친수")

# 트래킹
ans = '1'
l = 1 # ans의 길이
while l < i:
    # 마지막 자리가 1이면 다음 자리는 0
    if ans[-1] == '1':
        ans += '0'
    # 0이면 둘 다 올 수 있으므로 범위를 계산
    else:
        # 다음 자리를 0으로 하는 경우의 수를 계산하여
        # 경우의 수 > num일 경우 0, 아닐 경우 1
        if dp[i-l+1] > num:
            ans += '0'
        else:
            ans += '1'
            num -= dp[i-l+1]
    l += 1

print(''.join(ans))
