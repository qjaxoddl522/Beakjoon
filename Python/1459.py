import sys
input = lambda: sys.stdin.readline().rstrip()

X, Y, W, S = map(int, input().split())

# 대각선 이동 비용 재계산
S = min(W*2, S)

# 일단 둘 중에 짧은 쪽으로 대각 이동
result = min(X, Y) * S
# 남은 거리
dist = X + Y - min(X, Y) * 2
isDistOdd = (dist%2 == 1)

# 대각 이동이 직선 이동보다 효율적일 경우
if W > S:
    # 남은 거리가 홀수면 대각 이동만으로는 불가능
    result += (dist - (1 if isDistOdd else 0)) * S + \
              (W if isDistOdd else 0)
else:
    result += dist * W

print(result)
