import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
ans = 0
if A%2 == 0:
    A += 1
    ans += 1
if B%2 == 1:
    B -= 1
    ans += 1
ans += (B-A+1)//2
print(ans)