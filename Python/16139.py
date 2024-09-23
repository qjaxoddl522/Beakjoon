import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

arr_sum = [[0] * 26]
for i in range(len(S)):
    arr_temp = arr_sum[i][:]
    arr_temp[ord(S[i]) - ord('a')] += 1
    arr_sum.append(arr_temp)

for _ in range(q):
    c, l, r = input().rstrip().split()
    l, r = map(int, (l, r))
    idx = ord(c) - ord('a')
    print(arr_sum[r+1][idx] - arr_sum[l][idx])
