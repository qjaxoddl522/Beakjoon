import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
arr = []
for _ in range(N):
    arr_temp = [0, 0, 0]
    arr_temp[int(input())-1] += 1
    arr.append(arr_temp)
arr_sum = [[0, 0, 0]]
for i in range(N):
    arr_temp = [x+y for x, y in zip(arr_sum[i], arr[i])]
    arr_sum.append(arr_temp)

for _ in range(Q):
    i, j = map(int, input().rstrip().split())
    arr_temp = [x-y for x, y in zip(arr_sum[j], arr_sum[i-1])]
    print(*arr_temp)
