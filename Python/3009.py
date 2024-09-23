import sys
x, y = [0, 0, 0], [0, 0, 0]
x[0], y[0] = map(int, sys.stdin.readline().split())
x[1], y[1] = map(int, sys.stdin.readline().split())
x[2], y[2] = map(int, sys.stdin.readline().split())
x3, y3 = None, None
for xx in x:
    if x.count(xx) == 1:
        x3 = xx
        break
for yy in y:
    if y.count(yy) == 1:
        y3 = yy
        break
print(x3, y3)
