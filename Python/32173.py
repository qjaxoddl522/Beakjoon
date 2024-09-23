import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
satisList = list(map(int, input().split()))

ans = 0
satisSum = 0
for s in satisList:
    if ans < s - satisSum:
        ans = s - satisSum
    satisSum += s
print(ans)