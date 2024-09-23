import sys
n = int(sys.stdin.readline())
x, y = [], []
for _ in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    x.append(xy[0])
    y.append(xy[1])
print((max(x)-min(x))*(max(y)-min(y)))
