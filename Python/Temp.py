import sys
input = lambda: sys.stdin.readline().rstrip()

R, K, M = map(int, input().split())
i = K-1
reward = R
while i < M and reward > 0:
    i += K
    reward //= 2
print(reward)