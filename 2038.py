import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

# dp[f(k)] = k
dp = [0, 1]
summ = 1
k = 1
while summ < n:
    k += 1
    dp.append(1 + dp[k-dp[dp[k-1]]])
    summ += dp[k]

print(k)