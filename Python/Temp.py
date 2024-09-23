from collections import deque

n = int(input())
stairs = [0] * n
dp = [0] * n # dp 배열 초기화

for i in range(n):
    stairs[i] = int(input())

if n == 1: # 계단이 하나면
    dq = deque([(0, stairs[0], 1)])
else: # 계단이 두 개 이상이면
    dq = deque([(0, stairs[0], 1), (1, stairs[1], 1)])

while dq:
    now, cost, cnt = dq.popleft()
    if cost > dp[now]:
        dp[now] = cost
        if now + 1 < n and cnt < 2: # 계단을 세 개 연속으로 못 오른다.
            dq.append((now + 1, dp[now] + stairs[now + 1], cnt + 1))
        if now + 2 < n:
            dq.append((now + 2, dp[now] + stairs[now + 2], 1))
        
print(dp[n - 1])