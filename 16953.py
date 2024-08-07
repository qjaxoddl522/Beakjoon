def calc(N, cnt):
    if N > B:
        return
    d[N] = cnt

    calc(N*2, cnt+1)
    calc(int(str(N)+'1'), cnt+1)

A, B = map(int, input().split())
d = dict()

calc(A, 1)
if B in d:
    print(d[B])
else:
    print(-1)
