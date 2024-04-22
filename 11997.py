import sys
input = sys.stdin.readline

N = int(input())

#압축 전 좌표
x, y = [], []
xSet, ySet = [], []
for _ in range(N):
    i, j = map(int, input().rstrip().split())
    x.append(i)
    y.append(j)
#중복 제거 후 정렬
xSet = sorted(set(x))
ySet = sorted(set(y))

#압축된 좌표
xHash, yHash = {}, {}
for i, j in enumerate(xSet):
    xHash[j] = i
for i, j in enumerate(ySet):
    yHash[j] = i

#압축 후 좌표에 존재하는 소의 수 저장
arrComp = [[0] * N for _ in range(N)]
for i in range(N):
    arrComp[xHash[x[i]]][yHash[y[i]]] += 1

#압축 후 좌표에 대한 누적합 구하기
arrSum = [[0] * (len(yHash)+1) for _ in range(len(xHash)+1)]
for i in range(len(xHash)):
    for j in range(len(yHash)):
        arrSum[i+1][j+1] = arrSum[i+1][j] + arrSum[i][j+1] - arrSum[i][j] + arrComp[i][j]

#가로세로 선을 그어서 각 사분면 최대 소의 수 구하기
ans = int(1e9)
for i in range(len(xHash)+1):
    for j in range(len(yHash)+1):
        #각 사분면 비교
        tempMax = max(arrSum[i][j], arrSum[len(xHash)][j] - arrSum[i][j])
        tempMax = max(tempMax, arrSum[i][len(yHash)] - arrSum[i][j])
        tempMax = max(tempMax,
                      arrSum[len(xHash)][len(yHash)] - arrSum[len(xHash)][j] - arrSum[i][len(yHash)] + arrSum[i][j])

        #정답 갱신
        ans = min(ans, tempMax)
print(ans)
