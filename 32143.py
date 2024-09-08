import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

H = int(input())
N, Q = map(int, input().split())
at = list(map(int, input().split()))
heapq.heapify(at)
usedCard = len(at)
H -= sum(at)

if H > 0:
    print(-1)
else:
    while H + at[0] <= 0:
        outDamage = heapq.heappop(at)
        H += outDamage
        usedCard -= 1
    print(usedCard)

for _ in range(Q):
    newDamage = int(input())
    heapq.heappush(at, newDamage)
    H -= newDamage
    usedCard += 1

    if H > 0:
        print(-1)
    else:
        while H + at[0] <= 0:
            outDamage = heapq.heappop(at)
            H += outDamage
            usedCard -= 1
        print(usedCard)
