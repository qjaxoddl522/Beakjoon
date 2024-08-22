import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, M = map(int, input().split())
MAX_M = M.bit_length()
start = list(map(int, input().split()))
# link[i][j] = i번 동영상에서 2^j번 이동하면 뜨는 동영상 번호
link = [[-1] * MAX_M for _ in range(K+1)]
for i, k in enumerate(map(int, input().split())):
    link[i+1][0] = k

for j in range(1, MAX_M):
    for i in range(1, K+1):
        link[i][j] = link[link[i][j-1]][j-1]

# 쿼리 결과
result = []
for n in start:
    # M분에 마지막으로 시청한 동영상(예제 출력상의 의도)
    m = M-1
    for j in range(MAX_M-1, -1, -1):
        if m & 1<<j:
            m -= 1<<j
            n = link[n][j]
    result.append(n)

print(*result)
