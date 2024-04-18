import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
#인접한 값들의 차
arr_sub = [abs(arr[i]-arr[i+1]) for i in range(N-1)]
arr_sum = [0] #arr_sub의 구간합 배열
for i in range(N-1):
    arr_sum.append(arr_sum[i] + arr_sub[i])

for _ in range(M):
    i, j = map(int, input().rstrip().split())
    print(arr_sum[j-1] - arr_sum[i-1])
