import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr_sum = [0]
for i in range(1, N+1):
    arr_sum.append(arr_sum[i-1] + arr[i-1])

for _ in range(M):
    i, j = map(int, input().rstrip().split())
    print(arr_sum[j] - arr_sum[i-1]) #1, 3은 실제 인덱스 0, 2를 가리킴
