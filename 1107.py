import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M > 0:
    broken = set(input().split())
else:
    broken = set()

#최대 경우의 수
ans = abs(N - 100)

#채널 자체는 무한대
for i in range(1000001):
    for num in str(i):
        #부서진 버튼이면 못 만드는 숫자
        if num in broken:
            break
    #정상적으로 만들 수 있는 숫자면 ans 갱신
    else:
        ans = min(ans, len(str(i)) + abs(i - N))

print(ans)
