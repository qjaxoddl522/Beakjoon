import sys
input = lambda: sys.stdin.readline().rstrip()

# N 이하의 거의 소수의 수 구하기
def sieve(M, N):
    n = int(N**(1/2))
    
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(n**(1/2))+1):
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j] = False
    
    cnt = 0
    for sosu in range(2, n+1):
        if isPrime[sosu]:
            temp = sosu * sosu
            while temp <= N:
                if temp >= M:
                    cnt += 1
                temp *= sosu
    return cnt

A, B = map(int, input().split())
print(sieve(A, B))
