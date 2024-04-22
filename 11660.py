import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

arr_sum = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        #구간합 구하기
        arr_sum[i+1][j+1] = arr_sum[i][j+1] + arr_sum[i+1][j] - arr_sum[i][j] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    #큰 사각형에서 작은 사각형 둘 빼고 겹치는 부분 다시 더하기
    ans = arr_sum[x2][y2] - arr_sum[x1-1][y2] - arr_sum[x2][y1-1] + arr_sum[x1-1][y1-1]
    print(ans)
