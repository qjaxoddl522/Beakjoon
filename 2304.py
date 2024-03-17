import sys
input = sys.stdin.readline

N = int(input())
pillar = [list(map(int, input().rstrip().split())) for _ in range(N)]
pillar.sort()

ans = 0

stackLeft = [pillar[0]]
#왼쪽에서 오른쪽으로 훑기
for p in pillar[1:]:
    if stackLeft[-1][1] < p[1]: #높이가 더 클때만 스택 추가
        stackLeft.append(p)
        #바로 직전 기둥과의 거리 * 직전 기둥의 높이
        ans += abs(stackLeft[-1][0] - stackLeft[-2][0]) * (stackLeft[-2][1])

stackRight = [pillar[-1]]
#오른쪽에서 왼쪽으로 훑기
for p in pillar[-2::-1]:
    if stackRight[-1][1] < p[1]:
        stackRight.append(p)
        ans += abs(stackRight[-1][0] - stackRight[-2][0]) * (stackRight[-2][1])

#키가 큰 기둥들 중 가장 왼쪽과 가장 오른쪽 기둥 사이의 너비 * 높이
ans += abs(stackRight[-1][0] - stackLeft[-1][0] + 1) * (stackLeft[-1][1])

print(ans)
