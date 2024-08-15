import sys
input = lambda: sys.stdin.readline().rstrip()

def sieve(n):
    ls = set(range(2, n+1))
    for i in range(2, int(n**(1/2))):
        if i in ls:
            for j in range(i*i, n+1, i):
                ls.discard(j)
    return ls

def sangeun(n):
    overlap = set()
    while True:
        result = 0
        while n > 0:
            result += (n%10) ** 2
            n //= 10
        if result in overlap:
            return False
        if result == 1:
            return True
        overlap.add(result)
        n = result

N = int(input())
sosu = list(sieve(N))
ans = []
for i in sosu:
    if sangeun(i):
        ans.append(i)
for i in ans:
    print(i)
