import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
arr_sum = [0]
for i in range(N):
    arr_sum.append(arr_sum[i] + arr[i])

for _ in range(int(input())):
    i, j = list(map(int, input().rstrip().split()))
    print(arr_sum[j] - arr_sum[i-1])
