import sys
input = sys.stdin.readline
import heapq

hq = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        #(절댓값, 원래값) 함께 저장
        heapq.heappush(hq, (abs(n), n))
