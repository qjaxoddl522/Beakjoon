import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N//2):
    start = min(A[i], A[N-i-1])
    end = max(A[i], A[N-i-1])
    
    quot = (end-start)//K
    mod = (end-start)%K
    ans += min(quot + mod, quot+1 + K-mod)
print(ans)