import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sortA = sorted(A, reverse=True)
sortB = sorted(B)

ans = 0
for a, b in zip(sortA, sortB):
    ans += a * b
print(ans)
