# 두 벡터의 외적
def vec(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# AB와 BC의 외적
res = vec(x2 - x1, y2 - y1, x3 - x2, y3 - y2)
if res > 0:
    print(1)
elif res < 0:
    print(-1)
else:
    print(0)
