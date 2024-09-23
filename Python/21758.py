import sys
input = lambda: sys.stdin.readline().rstrip()

# 4칸 이상의 벌통은 양쪽 끝 중 하나가 최대 꿀을 보장함
# 벌 한 마리는 무조건 꿀통의 반대편 끝
# 나머지 벌 한 마리의 위치에 따라 벌통 위치를 정할 수 있음

N = int(input())
honeyList = list(map(int, input().split()))
honeyPrefix = [0]
for i in range(N):
    honeyPrefix.append(honeyPrefix[i] + honeyList[i])

honeyMax = -1

# 왼쪽 ~ N 탐색
for idx in range(1, N//2+1):
    honey = (honeyPrefix[N] - honeyPrefix[idx+1]) +\
            (honeyPrefix[N] - honeyList[0] - honeyList[idx])
    if honey > honeyMax:
        honeyMax = honey

# 0 ~ 오른쪽 탐색
for idx in range(N//2, N-1):
    honey = (honeyPrefix[idx]) +\
            (honeyPrefix[N] - honeyList[N-1] - honeyList[idx])
    if honey > honeyMax:
        honeyMax = honey

print(honeyMax if N > 3 else max(honeyList) * 2)
