import sys
input = sys.stdin.readline
#from queue import PriorityQueue
import heapq

queue = []

N = int(input())
for _ in range(N):
    x = int(input())

    if x == 0:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue) * -1)
    else:
        heapq.heappush(queue, -x)
