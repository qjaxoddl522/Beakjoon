import sys
input = lambda: sys.stdin.readline().rstrip()

L, N, rf, rb = map(int, input().split())
rest = [] # 지점, 풀
for _ in range(N):
    rest.append(list(map(int, input().split())))
rest.sort(key=lambda x:-x[1])

loc = 0
grass = 0
# 가장 많은 풀을 얻을 수 있는 곳부터 간다
for l, g in rest:
    if loc < l:
        # 대기 가능한 만큼 풀 얻기
        grass += (abs(rf*(l-loc)) - abs(rb*(l-loc))) * g
        loc = l

print(grass)
