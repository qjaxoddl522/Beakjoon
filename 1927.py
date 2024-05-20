import sys
input = sys.stdin.readline
from queue import PriorityQueue

q = PriorityQueue()

N = int(input())
for _ in range(N):
    C = int(input())
    if C == 0:
        if q.empty():
            print(0)
            continue
        print(q.get())
    else:
        q.put(C)
