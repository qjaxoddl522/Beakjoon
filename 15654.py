import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

# 백트래킹
# (한 줄당 숫자 수, 지금까지 배열에 들어간 숫자 수)
def bt(n, m):
    if m == M:
        print(*bt_arr)
        return

    for i in range(N):
        if arr[i] not in bt_arr:
            bt_arr.append(arr[i])
            bt(i+1, m+1)
            bt_arr.pop()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

bt_arr = deque([])
bt(0, 0)
