import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().rstrip().split()))
P.sort()

ans, lp = 0, len(P)
for i in range(lp):
    #더해야 하는 횟수 반영
    ans += (lp - i) * P[i]

print(ans)
