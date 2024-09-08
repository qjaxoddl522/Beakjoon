import sys
input = lambda: sys.stdin.readline().rstrip()

G = int(input())

s = 1
e = 1
valueExists = False
while True:
    g = (e**2 - s**2)
    if (e - s) == 1 and g > G:
        break

    if g == G:
        print(e)
        valueExists = True
    if g > G:
        s += 1
    elif g <= G:
        e += 1

if not valueExists:
    print(-1)