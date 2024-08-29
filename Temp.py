import sys
input = lambda: sys.stdin.readline().rstrip()

# 서브웨이 수, X이상 Y이하 만큼 잘라서 먹는다
N, X, Y = map(int, input().split())
subwayList = list(map(int, input().split()))

day = 0
trash = 0
for subway in subwayList:
    num = (max(subway-(2*Y), 0))//X
    subway -= X*num
    day += num
    print(subway)
print(day)
print(trash)
