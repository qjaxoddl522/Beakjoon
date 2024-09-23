import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 100000

# 벡터의 외적(크기)
def outerProduct(a, b):
    return a[0] * b[1] - b[0] * a[1]

# 벡터의 내적
def dotProduct(a, b):
    return a[0] * b[0] + a[1] * b[1]

# 두 선분이 겹치는지 확인
def checkCross(a, b, c, d):
    # AB관점에서 C, D가 다른 방향인지 확인
    ab = (b[0]-a[0], b[1]-a[1])
    ac = (c[0]-a[0], c[1]-a[1])
    ad = (d[0]-a[0], d[1]-a[1])
    if outerProduct(ab, ac) * outerProduct(ab, ad) >= 0:
        return False
    # CD관점에서 A, B가 다른 방향인지 확인
    cd = (d[0]-c[0], d[1]-c[1])
    ca = (a[0]-c[0], a[1]-c[1])
    cb = (b[0]-c[0], b[1]-c[1])
    if outerProduct(cd, ca) * outerProduct(cd, cb) >= 0:
        return False
    return True

# 점들의 거리
def pointDist(a, b):
    return (((b[0]-a[0])**2) + ((b[1]-a[1])**2)) ** (1/2)

# 점 c에서 ab로 수선의 발을 내린 거리
def lineDist(a, b, c):
    # 수선의 발이 선분 상에 있을 때만
    t = dotProduct((c[0]-a[0], c[1]-a[1]), (b[0]-a[0], b[1]-a[1]))/\
        dotProduct((b[0]-a[0], b[1]-a[1]), (b[0]-a[0], b[1]-a[1]))
    if 0 <= t <= 1:
        upper = abs((b[0]-a[0])*(a[1]-c[1])-(a[0]-c[0])*(b[1]-a[1]))
        lower = pointDist(a, b)
        return upper / lower
    return MAX

def solve():
    n, m = map(int, input().split())
    ls1 = [tuple(map(float, input().split())) for _ in range(n)]
    ls2 = [tuple(map(float, input().split())) for _ in range(m)]
    
    result = MAX
    for line1 in ls1:
        for line2 in ls2:
            A = (line1[0], line1[1])
            B = (line1[2], line1[3])
            C = (line2[0], line2[1])
            D = (line2[2], line2[3])

            # 겹치면 도로를 놓지 않아도 됨
            if checkCross(A, B, C, D):
                return 0
            
            # AC, BC, AD, BD 거리
            result = min(result,
                         pointDist(A, C), pointDist(B, C),
                         pointDist(A, D), pointDist(B, D))
            
            # 각 점에서 수선의 발 거리 측정(선분에 닿지 않을시 MAX 반환)
            result = min(result, lineDist(A, B, C), lineDist(A, B, D),
                         lineDist(C, D, A), lineDist(C, D, B))            
            
    return result

print(solve())
