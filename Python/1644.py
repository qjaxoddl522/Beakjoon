import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# 에라토스테네스의 체
sosu = [False, False] + [True] * (N-1)
for i in range(2, int(N**(1/2))+1):
    if sosu[i]:
        for j in range(i**2, N+1, i):
            sosu[j] = False
sosu = [i for i in range(2, N+1) if sosu[i]]

# 투포인터
cnt = 0
value = 0
s = 0
for e in sosu:
    value += e

    while value > N:
        value -= sosu[s]
        s += 1
    
    if value == N:
        cnt += 1
print(cnt)