import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(k):
    if k in sosu:
        print(0)
        return

    # 작은 수 찾기
    kMin = k-1
    while True:
        if kMin in sosu:
            break
        kMin -= 1

    # 큰 수 찾기
    kMax = k+1
    while True:
        if kMax in sosu:
            break
        kMax += 1

    print(kMax - kMin)

# 에라토스테네스의 체
def eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**(1/2))+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    return set(i for i in range(n+1) if sieve[i])

sosu = eratosthenes(1299709)

for _ in range(int(input())):
    solve(int(input()))
