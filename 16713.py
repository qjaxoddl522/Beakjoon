import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

#구간 XOR배열
arrSum = [0] * (N+1)
for i in range(1, N+1):
    arrSum[i] = arrSum[i-1] ^ arr[i-1]

ans = 0
for _ in range(Q):
    s, e = map(int, input().rstrip().split())
    ans = ans ^ (arrSum[e] ^ arrSum[s-1])
print(ans)
