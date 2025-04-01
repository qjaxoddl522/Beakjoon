import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N = int(input())
    medicine = input()

    result = 0
    visited = set()
    dq = deque([(0, N*3-1)])
    while dq:
        left, right = dq.popleft()
        
        if (left, right) in visited:
            continue
        visited.add((left, right))

        eat = left + (N*3-1 - right)
        result = max(result, eat)

        if eat == N*3:
            break

        if eat % 3 == 0:
            if medicine[left] == 'B':
                dq.append((left+1, right))
            if medicine[right] == 'B':
                dq.append((left, right-1))
        elif eat % 3 == 1:
            if medicine[left] == 'L':
                dq.append((left+1, right))
            if medicine[right] == 'L':
                dq.append((left, right-1))
        elif eat % 3 == 2:
            if medicine[left] == 'D':
                dq.append((left+1, right))
            if medicine[right] == 'D':
                dq.append((left, right-1))

    print(result)

main()