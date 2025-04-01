import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    W = list(input().split())
    ls = list(input().split())
    ls = ls + ls
    
    fail = [0] * len(W)
    j = 0
    for i in range(1, len(W)):
        while j > 0 and W[i] != W[j]:
            j = fail[j-1]
        if W[i] == W[j]:
            j += 1
            fail[i] = j
    
    result = 0
    j = 0
    for i in range(1, len(ls)):
        while j > 0 and ls[i] != W[j]:
            j = fail[j-1]
        if ls[i] == W[j]:
            if j == len(W)-1:
                result += 1
                j = fail[j]
            else:
                j += 1
    
    def gcd(a, b):
        while b != 0:
            t = a % b
            a, b = b, t
        return a
    
    g = gcd(result, len(ls)//2)
    print(f"{result//g}/{len(ls)//2//g}")

main()