import sys
input = sys.stdin.readline

R, C, Q = map(int, input().rstrip().split())

arr = []
for i in range(R):
    arr.append(list(map(int, input().rstrip().split())))

aSum = [[0] * (C+1) for _ in range(R+1)] #구간합
for i in range(R):
    for j in range(C):
        aSum[i+1][j+1] = aSum[i][j+1] + aSum[i+1][j] - aSum[i][j] + arr[i][j]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().rstrip().split())
    size = (r2 - r1 + 1) * (c2 - c1 + 1)
    print((aSum[r2][c2] - aSum[r1-1][c2] - aSum[r2][c1-1] + aSum[r1-1][c1-1]) // size)
