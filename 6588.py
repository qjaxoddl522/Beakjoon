import sys
input = lambda: sys.stdin.readline().rstrip()

def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False 
    for i in range(2, int(n**(1/2)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

sosu = sieve(1000000)
sosu[2] = False
while True:
    n = int(input())
    if n == 0:
        break

    isFound = False
    for i in range(3, n//2 + 1, 2):
        if sosu[i] and sosu[n-i]:
            print(f"{n} = {i} + {n-i}")
            isFound = True
            break
    if not isFound:
        print("Goldbach's conjecture is wrong.")
