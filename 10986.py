import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr_sum = [0]
for i in range(N):
    arr_sum.append(arr_sum[i] + arr[i])

remain = [0 for _ in range(M)]
ans = 0

#구간 s,e의 합이 M으로 나누어 떨어진다는 말은
#arr_sum[s] % M = arr_sum[e] % M 와 같다.
#따라서 나머지가 같은 구간합끼리 모아 구간 선택의 경우의 수를 합한다
for s in arr_sum:
    remain[s%M] += 1
for n in remain:
    #n개의 원소 중 2개를 선택하는 경우의 수
    ans += n*(n-1)//2

print(ans)
