import sys
input = sys.stdin.readline
import heapq

hq = []
N = int(input())
for _ in range(N):
    heapq.heappush(hq, int(input()))

#총 비교 횟수
ans = 0

#큐에 한 개만 남을 때까지 가장 작은 둘을 합치고 다시 넣는 작업을 반복
while (len(hq) > 1):
    num = heapq.heappop(hq) + heapq.heappop(hq)
    heapq.heappush(hq, num)
    ans += num

print(ans)
