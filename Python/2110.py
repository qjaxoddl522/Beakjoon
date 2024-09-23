import sys
input = sys.stdin.readline

N, C = map(int, input().split())
co = sorted(int(input()) for _ in range(N))

bot, top = 1, co[-1] - co[0]
ans = 0

while(bot <= top):
    mid = (bot + top) // 2 #두 공유기 사이 가능한 최대 거리

    now = co[0] #현재 좌표
    iptime = 1 #설치한 공유기 수
    for i in range(1, len(co)):
        if now + mid <= co[i]: #다음 집이 거리가 되면 설치
            now = co[i]
            iptime += 1

    if iptime >= C:
        bot = mid + 1
        ans = mid
    else:
        top = mid - 1

print(ans)
